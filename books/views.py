from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAdminUser()]
        return [permissions.IsAuthenticated()]

    def destroy(self, request, *args, **kwargs):
        book = self.get_object()

        # Prevent deletion if any copy is borrowed
        if book.available_copies < book.total_copies:
            return Response(
                {"error": "Cannot delete borrowed book"},
                status=status.HTTP_400_BAD_REQUEST
            )

        return super().destroy(request, *args, **kwargs)