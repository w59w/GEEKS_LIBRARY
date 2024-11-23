from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Avg
from .models import Book
from .forms import CommentForm


# Главная страница
class HomeView(TemplateView):
    template_name = 'main_page/home.html'


# Список книг
class BookListView(ListView):
    model = Book
    template_name = 'main_page/book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        hashtag = self.request.GET.get('hashtag')
        if hashtag:
            return Book.objects.filter(hashtags__icontains=hashtag)
        return Book.objects.all()


class BookDetailView(DetailView):
    model = Book
    template_name = 'main_page/book_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        book = self.object

        comments = book.comments.all().order_by('-created_at')[:5]
        average_rating = comments.aggregate(Avg('rating'))['rating__avg']

        context['comments'] = comments
        context['average_rating'] = average_rating
        context['form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.book = self.object
            comment.save()
        return self.get(request, *args, **kwargs)
