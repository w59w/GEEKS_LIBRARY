from django.http import HttpResponse
from datetime import datetime


def home(request):
    return HttpResponse("Добро пожаловать на главную страницу!")


def about_me(request):
    return HttpResponse("Меня зовут Кумушай. Я программист и увлекаюсь искусственным интеллектом.")


def about_my_pets(request):
    html_content = """
    <h1>Мой питомец</h1>
    <p>Имя: Барсик</p>
    <img src="https://example.com/path/to/your/cat/image.jpg" alt="Фото моего питомца" width="300">
    """
    return HttpResponse(html_content)


def system_time(request):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return HttpResponse(f"Текущая дата и время: {current_time}")
