from django.shortcuts import render
from .models import *
from .forms import BookFrom
# Create your views here.


def index(request):
    context = {
        'category': Category.objects.all(),
        'id_books': Book.objects.all(),
        'form': BookFrom(),
    }
    return render(request, 'pages/index.html', context)


def books(request):
    context = {
        'category': Category.objects.all(),
        'id_books': Book.objects.all(),
    }
    return render(request, 'pages/books.html', context)
