from django.shortcuts import render
from django.views.generic.list import ListView
from book.models import Book
from reference.models import Author
from django.db.models import Q


class LastView(ListView):
    model = Book
    template_name = 'main/main.html'

    def get_queryset(self):
        qs = super().get_queryset()
        q = qs.order_by('-created_date')
        search = self.request.GET.get('search', 0)
        if search != 0:
            return q.filter(name=search)
        else:
            return q
