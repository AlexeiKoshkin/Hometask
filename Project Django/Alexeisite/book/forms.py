from django import forms
from django.forms import ModelForm
from .models import Book


class SearchForm(forms.Form):
    search = forms.CharField(label="Поиск по названию")


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('name',
                  'image',
                  'price',
                  'authors',
                  'serie',
                  'genre',
                  'issue_year',
                  'page',
                  'binding',
                  'size',
                  'isbn',
                  'weight',
                  'age_rest',
                  'publisher',
                  'num_book',
                  'available',
                  'rating',
                  )
