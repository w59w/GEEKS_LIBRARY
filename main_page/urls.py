from django.urls import path
from .views import home, about_me, about_my_pets, system_time

urlpatterns = [
    path('', home, name='home'),  # Главная страница
    path('about_me/', about_me, name='about_me'),
    path('about_my_pets/', about_my_pets, name='about_my_pets'),
    path('system_time/', system_time, name='system_time'),
]
