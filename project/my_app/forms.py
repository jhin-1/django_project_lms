from django import forms
from .models import *


class BookFrom(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'photo_book',
            'author_book',
            'pages_of_book',
            'price',
            'rental_price_day',
            'rental_preiod',
            'status',
            'category',

        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'photo_book': forms.FileInput(attrs={'class': 'form-control'}),
            'author_book': forms.FileInput(attrs={'class': 'form-control'}),
            'pages_of_book': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'rental_price_day': forms.NumberInput(attrs={'class': 'form-control'}),
            'rental_preiod': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }



