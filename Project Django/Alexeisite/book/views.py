from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from book.models import Book
from book.forms import *
from django.urls import reverse_lazy


class BookDetail(DetailView):
    model = Book


class BookList(ListView):
    model = Book

    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get('search', 0)
        if search != 0:
            return qs.filter(name=search)
        else:
            return qs

    def get_context_data(self):
        context = super().get_context_data()
        f = SearchForm()
        context["form"] = f
        return context


class BookCreate(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book/create_form.html'

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('book_detail_view',
                                kwargs={'pk': self.object.pk})
        elif self.request.POST.get('list'):
            return reverse_lazy('book_list_view')
        return reverse_lazy('book_create_view')


class BookUpdate(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book/update_form.html'

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('book_detail_view',
                                kwargs={'pk': self.object.pk})
        return reverse_lazy('book_list_view')


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('book_list_view')
    template_name = 'book/delete_form.html'
