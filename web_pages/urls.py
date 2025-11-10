from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

# need to be explicit to use CBVs
from .views import BookListView, BookAddView, BookDetailView

urlpatterns = [
    # path('', views.homepage, name='home'),
    path('', BookListView.as_view(), name='book_list'),
    path('books/<int:id>/', BookDetailView.as_view(), name='book_detail'),
    path('books/add/', BookAddView.as_view(), name='add_book'),
    path('books/<int:id>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:id>/delete', views.delete_book, name='delete_book'),
]

# for serving media files during Development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
