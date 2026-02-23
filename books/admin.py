from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'isbn',
        'total_copies',
        'available_copies',
        'is_fully_available',
    )

    search_fields = ('title', 'author', 'isbn')
    list_filter = ('author',)

    def is_fully_available(self, obj):
        return obj.available_copies == obj.total_copies

    is_fully_available.boolean = True