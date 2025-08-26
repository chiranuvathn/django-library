from django.http import HttpResponse
from django.shortcuts import render
from .models import Book

def homepage(request):
    return HttpResponse('Welcome to the Library!')

def book_list(request):
    books = Book.objects.all()
    context = {'books': books}
    
    return render(request, 'pages/book_list.html', context)