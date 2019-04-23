from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from reference.models import Author, Serie, Genre, Publisher
from reference.forms import SearchForm
# Create your views here.


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


class ReferenceVeiw(TemplateView):
    template_name = 'reference/reference.html'
