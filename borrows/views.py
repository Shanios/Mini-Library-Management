from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.utils.timezone import now
from .models import Borrow
from books.models import Book


class BorrowBookView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, book_id):
        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return Response({"error": "Book not found"}, status=404)

        if book.available_copies <= 0:
            return Response({"error": "No copies available"}, status=400)

        already_borrowed = Borrow.objects.filter(
            user=request.user,
            book=book,
            returned_at__isnull=True
        ).exists()

        if already_borrowed:
            return Response({"error": "You already borrowed this book"}, status=400)

        Borrow.objects.create(user=request.user, book=book)
        book.available_copies -= 1
        book.save()

        return Response({"message": "Book borrowed successfully"}, status=200)


class ReturnBookView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, book_id):

        if request.user.is_staff:
            # Admin can return any active borrow
            borrow = Borrow.objects.filter(
                book_id=book_id,
                returned_at__isnull=True
            ).first()
        else:
            # Normal user can only return their own borrow
            borrow = Borrow.objects.filter(
                user=request.user,
                book_id=book_id,
                returned_at__isnull=True
            ).first()

        if not borrow:
            return Response(
                {"error": "No active borrow found"},
                status=400
            )

        borrow.returned_at = now()
        borrow.save()

        book = borrow.book
        book.available_copies += 1
        book.save()

        return Response(
            {"message": "Book returned successfully"},
            status=200
        )


class MyBorrowsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        borrows = Borrow.objects.filter(
            user=request.user,
            returned_at__isnull=True
        )

        data = []
        for b in borrows:
            data.append({
                "book_id": b.book.id,
                "book_title": b.book.title,
                "borrowed_at": b.borrowed_at
            })

        return Response(data)