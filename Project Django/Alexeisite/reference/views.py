from django.views.generic.detail import DetailView
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
