from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_order, name='create_order'),
    path('', views.order_list, name='order_list'),
    path('<int:pk>/edit/', views.edit_order, name='edit_order'),
    path('<int:pk>/delete/', views.delete_order, name='delete_order'),
]
