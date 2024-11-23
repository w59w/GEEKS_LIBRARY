from django.core.management.base import BaseCommand
from main_page.models import Book
from scripts.book_parser import parse_books  # Подключаем нашу функцию

class Command(BaseCommand):
    help = 'Парсинг книг с сайта Books to Scrape'

    def handle(self, *args, **kwargs):
        parse_books()
        self.stdout.write(self.style.SUCCESS('Книги успешно спарсены и добавлены в базу данных'))
