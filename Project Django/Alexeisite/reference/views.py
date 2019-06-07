from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from reference.models import Author, Serie, Genre, Publisher
from reference.forms import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.


class ReferenceVeiw(TemplateView):
    template_name = 'reference/reference.html'


class AuthorDetail(DetailView):
    model = Author


class SerieDetail(DetailView):
    model = Serie


class GenreDetail(DetailView):
    model = Genre


class PublisherDetail(DetailView):
    model = Publisher


class AuthorList(ListView):
    model = Author

    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get('search', 0)
        if search != 0:
            return qs.filter(first_name=search)
        else:
            return qs

    def get_context_data(self):
        context = super().get_context_data()
        f = SearchForm()
        context["form"] = f
        return context


class SerieList(ListView):
    model = Serie

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


class GenreList(ListView):
    model = Genre

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


class PublisherList(ListView):
    model = Publisher

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


class AuthorCreate(PermissionRequiredMixin, CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'reference/create_form.html'
    permission_required = 'books.edit_content'

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('author_detail_view',
                                kwargs={'pk': self.object.pk})
        elif self.request.POST.get('list'):
            return reverse_lazy('author_list_view')
        return reverse_lazy('author_create_view')


class SerieCreate(PermissionRequiredMixin, CreateView):
    model = Serie
    form_class = SerieForm
    template_name = 'reference/create_form.html'
    permission_required = 'books.edit_content'

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('serie_detail_view',
                                kwargs={'pk': self.object.pk})
        elif self.request.POST.get('list'):
            return reverse_lazy('serie_list_view')
        return reverse_lazy('serie_create_view')


class GenreCreate(PermissionRequiredMixin, CreateView):
    model = Genre
    form_class = GenreForm
    template_name = 'reference/create_form.html'
    permission_required = 'books.edit_content'

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('genre_detail_view',
                                kwargs={'pk': self.object.pk})
        elif self.request.POST.get('list'):
            return reverse_lazy('genre_list_view')
        return reverse_lazy('genre_create_view')


class PublisherCreate(PermissionRequiredMixin, CreateView):
    model = Publisher
    form_class = PublisherForm
    template_name = 'reference/create_form.html'
    permission_required = 'books.edit_content'

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('publisher_detail_view',
                                kwargs={'pk': self.object.pk})
        elif self.request.POST.get('list'):
            return reverse_lazy('publisher_list_view')
        return reverse_lazy('publisher_create_view')


class AuthorUpdate(PermissionRequiredMixin, UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'reference/update_form.html'
    permission_required = 'books.edit_content'

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('author_detail_view',
                                kwargs={'pk': self.object.pk})
        return reverse_lazy('author_list_view')


class SerieUpdate(PermissionRequiredMixin, UpdateView):
    model = Serie
    form_class = SerieForm
    template_name = 'reference/update_form.html'
    permission_required = 'books.edit_content'

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('serie_detail_view',
                                kwargs={'pk': self.object.pk})
        return reverse_lazy('serie_list_view')


class GenreUpdate(PermissionRequiredMixin, UpdateView):
    model = Genre
    form_class = GenreForm
    template_name = 'reference/update_form.html'
    permission_required = 'books.edit_content'

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('genre_detail_view',
                                kwargs={'pk': self.object.pk})
        return reverse_lazy('genre_list_view')


class PublisherUpdate(PermissionRequiredMixin, UpdateView):
    model = Publisher
    form_class = PublisherForm
    template_name = 'reference/update_form.html'
    permission_required = 'books.edit_content'

    def get_success_url(self):
        if self.request.POST.get('detail'):
            return reverse_lazy('publisher_detail_view',
                                kwargs={'pk': self.object.pk})
        return reverse_lazy('publisher_list_view')


class AuthorDelete(PermissionRequiredMixin, DeleteView):
    model = Author
    success_url = reverse_lazy('author_list_view')
    template_name = 'reference/delete_form.html'
    permission_required = 'books.edit_content'


class SerieDelete(PermissionRequiredMixin, DeleteView):
    model = Serie
    success_url = reverse_lazy('serie_list_view')
    template_name = 'reference/delete_form.html'
    permission_required = 'books.edit_content'


class GenreDelete(PermissionRequiredMixin, DeleteView):
    model = Genre
    success_url = reverse_lazy('genre_list_view')
    template_name = 'reference/delete_form.html'
    permission_required = 'books.edit_content'


class PublisherDelete(PermissionRequiredMixin, DeleteView):
    model = Publisher
    success_url = reverse_lazy('publisher_list_view')
    template_name = 'reference/delete_form.html'
    permission_required = 'books.edit_content'
