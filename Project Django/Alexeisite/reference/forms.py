from django import forms
from django.forms import ModelForm
from .models import Author, Serie, Genre, Publisher


class SearchForm(forms.Form):
    search = forms.CharField(label="Поиск по названию")


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name')


class SerieForm(ModelForm):
    class Meta:
        model = Serie
        fields = ('name', 'description')


class GenreForm(ModelForm):
    class Meta:
        model = Genre
        fields = ('name',)


class PublisherForm(ModelForm):
    class Meta:
        model = Publisher
        fields = ('name', 'description')
