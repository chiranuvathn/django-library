from django.http import HttpResponse
from django.shortcuts import render

from .models import Book
from .forms import BookForm

def homepage(request):
    return HttpResponse('Welcome to the Library!')

def book_list(request):
    books = Book.objects.all()
    context = {'books': books}
    
    return render(request, 'pages/book_list.html', context)

# to add 'post' request handler and save form inputs to database
def add_book(request):
    form = BookForm()
    context = {'form': form}

    return render(request, 'pages/book_form.html', context)