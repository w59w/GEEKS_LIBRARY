from django.db import models


class Book(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=200)  # Название книги
    author = models.CharField(max_length=100)  # Автор книги
    published_date = models.DateField()  # Дата публикации
    isbn = models.CharField(max_length=13, unique=True)  # ISBN
    pages = models.PositiveIntegerField()  # Количество страниц
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)  # Обложка книги
    description = models.TextField()  # Описание книги
    hashtags = models.CharField(max_length=255, blank=True, null=True)  # Хэштеги

    def __str__(self):
        return self.title


class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    user_name = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Комментарий от {self.user_name} к {self.book.title}'


