from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('book_list'), name='home'),  # Перенаправление на список книг
    path('books/', include('main_page.urls')),
    path('basket/', include('basket.urls')),
]

