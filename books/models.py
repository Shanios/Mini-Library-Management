

# Create your models here.
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20, unique=True)
    total_copies = models.PositiveIntegerField()
    available_copies = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        if self.available_copies > self.total_copies:
            self.available_copies = self.total_copies
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title