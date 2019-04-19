from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from reference.models import Author, Serie, Genre, Publisher
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


class SerieList(ListView):
    model = Serie


class GenreList(ListView):
    model = Genre


class PublisherList(ListView):
    model = Publisher


class ReferenceVeiw(TemplateView):
    template_name = 'reference/reference.html'
