from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Book
from .forms import BookForm

def homepage(request):
    return HttpResponse('Welcome to the Library!')

def book_list(request):
    books = Book.objects.all()
    context = {'books': books}
    
    return render(request, 'pages/book_list.html', context)

def book_detail(request, id):
    book = get_object_or_404(Book, pk=id)
    context = {'book': book}

    return render(request, 'pages/book_detail.html', context)

def add_book(request):
    form = BookForm()

    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('book_list')
    
    context = {'form': form}

    return render(request, 'pages/book_form.html', context)
