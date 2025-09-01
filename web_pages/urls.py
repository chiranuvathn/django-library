from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:id>/', views.book_detail, name='book_detail'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:id>/edit/', views.edit_book, name='edit_book'),
]