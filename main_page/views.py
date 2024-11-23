from django.shortcuts import render, get_object_or_404
from django.db import models
from .models import Book
from .forms import CommentForm


def home(request):
    return render(request, 'main_page/home.html')


def book_list(request):
    hashtag = request.GET.get('hashtag')
    if hashtag:
        books = Book.objects.filter(hashtags__icontains=hashtag)
    else:
        books = Book.objects.all()
    return render(request, 'main_page/book_list.html', {'books': books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    comments = book.comments.all().order_by('-created_at')[:5]
    average_rating = comments.aggregate(models.Avg('rating'))['rating__avg']

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = book
            comment.save()
    else:
        form = CommentForm()

    return render(request, 'main_page/book_detail.html', {
        'book': book,
        'comments': comments,
        'form': form,
        'average_rating': average_rating
    })
