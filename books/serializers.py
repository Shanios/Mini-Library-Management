from rest_framework import serializers
from .models import Book
from borrows.models import Borrow


class BookSerializer(serializers.ModelSerializer):
    is_borrowed = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'author',
            'isbn',
            'total_copies',
            'available_copies',
            'is_borrowed'
        ]

    def get_is_borrowed(self, obj):
        return obj.available_copies < obj.total_copies