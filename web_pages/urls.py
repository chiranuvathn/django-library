from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views

# need to be explicit to use CBVs
from .views import BookListView, BookDetailView, BookAddView, BookEditView, BookDetailView, BookDeleteView

urlpatterns = [
    # path('', views.homepage, name='home'),
    path('', BookListView.as_view(), name='book_list'),
    path('books/<int:id>/', BookDetailView.as_view(), name='book_detail'),
    path('books/add/', BookAddView.as_view(), name='add_book'),
    path('books/<int:id>/edit/', BookEditView.as_view(), name='edit_book'),
    path('books/<int:id>/delete', BookDeleteView.as_view(), name='delete_book'),
]

# for serving media files during Development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
