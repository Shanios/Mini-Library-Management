from django.urls import path
from .views import BorrowBookView, ReturnBookView, MyBorrowsView

urlpatterns = [
    path('<int:book_id>/', BorrowBookView.as_view(), name='borrow-book'),
    path('return/<int:book_id>/', ReturnBookView.as_view(), name='return-book'),
    path('my-borrows/', MyBorrowsView.as_view(), name='my-borrows'),
]