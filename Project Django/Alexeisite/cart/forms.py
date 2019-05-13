from django import forms
from django.forms import ModelForm
from .models import BookInCart


class AddBookForm(forms.ModelForm):
    class Meta:
        model = BookInCart

        fields = [
            'book',
            'quantity'
        ]
        widgets = {
            'book': forms.HiddenInput(),
        }
