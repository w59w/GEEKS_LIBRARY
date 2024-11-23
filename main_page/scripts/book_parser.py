import requests
from bs4 import BeautifulSoup
from main_page.models import Book  # Импорт модели книги


def parse_books():
    base_url = "https://books.toscrape.com/catalogue/page-{}.html"
    page = 1
    books_parsed = 0

    while True:
        # Формируем URL для текущей страницы
        url = base_url.format(page)
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Страница {page} недоступна, парсинг завершен.")
            break

        # Обрабатываем HTML-ответ
        soup = BeautifulSoup(response.text, 'html.parser')
        book_elements = soup.find_all('article', class_='product_pod')

        if not book_elements:
            print("Книги не найдены на странице. Парсинг завершен.")
            break

        # Парсим данные для каждой книги
        for book_el in book_elements:
            # Название книги
            title = book_el.find('h3').find('a')['title']
            # Цена
            price = book_el.find('p', class_='price_color').text[1:]  # Убираем знак £
            # Наличие
            availability = book_el.find('p', class_='instock availability').text.strip()
            in_stock = "In stock" in availability
            # Категория книги (выберем категорию через URL или другим способом)
            category = "Unknown"  # Можем добавить более сложную логику

            Book.objects.get_or_create(
                title=title,
                defaults={
                    'author': 'Unknown',
                    'price': float(price),
                    'stock': in_stock,
                    'category': category,
                },
            )
            books_parsed += 1

        print(f"Страница {page} обработана. Парсинг продолжается...")
        page += 1

    print(f"Парсинг завершен. Добавлено книг: {books_parsed}")
