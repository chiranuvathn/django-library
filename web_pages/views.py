from django.core.paginator import Paginator
from django.http import HttpResponse, Http404, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.views.generic import DetailView

from .models import Book
from .forms import BookForm

def homepage(request):
    return HttpResponse('Welcome to the Library!')

def book_list(request):
    books = Book.objects.all()

    # filtering
    title = request.GET.get('title')

    if title:
        books = books.filter(title__icontains=title)

    # sorting
    valid_sort_options = ['title', 'author', 'published_date']
    sort_by = request.GET.get('sort_option')

    if sort_by not in valid_sort_options:
        sort_by = 'title'

    books = books.order_by(sort_by)

    # paginator
    paginator = Paginator(books, 2)
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}
    
    return render(request, 'pages/book_list.html', context)

class BookDetailView(DetailView):
    model = Book
    pk_url_kwarg = 'id' # change from default 'pk'
    template_name = 'pages/book_detail.html'


def book_detail(request, id):
    book = get_object_or_404(Book, pk=id)
    context = {'book': book}

    return render(request, 'pages/book_detail.html', context)

@login_required
def add_book(request):
    form = BookForm()

    if request.method == 'POST':
        # package form inputs and update 'Book' model
        form = BookForm(request.POST, request.FILES)

        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()

            messages.success(request,"Your book was added successfully!")
            return redirect('book_list')
    
    context = {
        'form': form,
        'title': 'Add A New Book',
        'button': 'Submit'
    }

    return render(request, 'pages/book_form.html', context)

@login_required
def edit_book(request, id):
    try:
        book = get_object_or_404(Book, pk=id, user=request.user)
    except Http404:
        return HttpResponseForbidden("Access Denied. You do not have permission to edit this book.")
    
    if request.method == 'POST':
        # package form inputs and update 'Book' model by id
        form = BookForm(request.POST, request.FILES, instance=book)

        if form.is_valid():
            form.save()
            
            messages.success(request,"Your book was edited successfully!")
            return redirect('book_list')
    
    else:
        # populate form with 'Book' model by id
        form = BookForm(instance=book)
    
    context = {
        'form': form,
        'title': 'Editing - ' + book.title,
        'button': 'Save Changes'
    }

    return render(request, 'pages/book_form.html', context)

@login_required
def delete_book(request, id):
    try:
        book = get_object_or_404(Book, pk=id, user=request.user)
    except Http404:
        return HttpResponseForbidden("Access Denied. You do not have permission to delete this book.")
    book.delete()
    
    messages.success(request,"Your book has been deleted!")
    return redirect('book_list')
