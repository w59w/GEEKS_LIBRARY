from django.urls import path
from .views import HomeView, BookListView, BookDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
]
