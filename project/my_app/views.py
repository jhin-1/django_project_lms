from django.shortcuts import render, redirect
from .models import *
from .forms import BookFrom, CategoryForm
# Create your views here.


def index(request):

    if request.method == 'POST':
        add_book = BookFrom(request.POST, request.FILES)
        add_category = CategoryForm(request.POST)

        if add_book.is_valid():
            add_book.save()
            return redirect('index')

        if add_category.is_valid():
            add_category.save()
            return redirect('index')

    context = {
        'category': Category.objects.all(),
        'id_books': Book.objects.all(),
        'form': BookFrom(),
        'formcat': CategoryForm(),
    }
    return render(request, 'pages/index.html', context)


def books(request):
    context = {
        'category': Category.objects.all(),
        'id_books': Book.objects.all(),
    }
    return render(request, 'pages/books.html', context)


def update(request, id):
    book_id = Book.objects.get(id=id)
    if request.method == 'POST':
        book_save = BookFrom(request.POST, request.FILES, instance=book_id)
        if book_save.is_valid():
            book_save.save()
    else:
        book_save = BookFrom(instance=book_id)
    context = {
        'form': book_save,
    }
    return render(request, 'pages/update.html', context)
