

# Register your models here.
from django.contrib import admin
from .models import Borrow

@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'borrowed_at', 'returned_at')
    list_filter = ('returned_at',)