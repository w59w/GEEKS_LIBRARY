from django.db import models
from main_page.models import Book


class Order(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Заказ: {self.name} - {self.book.title}'
