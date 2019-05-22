from django import forms
from django.forms import ModelForm
from .models import Order


class CheckOutOrderForm(forms.ModelForm):
    class Meta:
        model = Order

        fields = [
            'cart',
            'status',
            'delivery_address',
            'email',
            'phone',
            'comments'
        ]
        widgets = {
            'cart': forms.HiddenInput(),
            'status': forms.HiddenInput()
        }
