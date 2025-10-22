from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

urlpatterns = [
    # path('', views.homepage, name='home'),
    path('', views.book_list, name='book_list'),
    path('books/<int:id>/', views.book_detail, name='book_detail'),
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:id>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:id>/delete', views.delete_book, name='delete_book'),
]

# for serving media files during Development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
