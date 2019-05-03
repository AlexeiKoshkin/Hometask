from django.urls import path
from reference.models import *
from reference.views import *

urlpatterns = [
    path('', ReferenceVeiw.as_view(),
         name='reference_view'),

    path('author/<int:pk>', AuthorDetail.as_view(),
         name='author_detail_view'),
    path('serie/<int:pk>', SerieDetail.as_view(),
         name='serie_detail_view'),
    path('genre/<int:pk>', GenreDetail.as_view(),
         name='genre_detail_view'),
    path('publisher/<int:pk>', PublisherDetail.as_view(),
         name='publisher_detail_view'),

    path('author/', AuthorList.as_view(),
         name='author_list_view'),
    path('serie/', SerieList.as_view(),
         name='serie_list_view'),
    path('genre/', GenreList.as_view(),
         name='genre_list_view'),
    path('publisher/', PublisherList.as_view(),
         name='publisher_list_view'),

    path('author/create/', AuthorCreate.as_view(),
         name='author_create_view'),
    path('serie/create/', SerieCreate.as_view(),
         name='serie_create_view'),
    path('genre/create/', GenreCreate.as_view(),
         name='genre_create_view'),
    path('publisher/create/', PublisherCreate.as_view(),
         name='publisher_create_view'),

    path('author/update/<int:pk>', AuthorUpdate.as_view(),
         name='author_update_view'),
    path('serie/update/<int:pk>', SerieUpdate.as_view(),
         name='serie_update_view'),
    path('genre/update/<int:pk>', GenreUpdate.as_view(),
         name='genre_update_view'),
    path('publisher/update<int:pk>', PublisherUpdate.as_view(),
         name='publisher_update_view'),

    path('author/delete/<int:pk>', AuthorDelete.as_view(),
         name='author_delete_view'),
    path('serie/delete/<int:pk>', SerieDelete.as_view(),
         name='serie_delete_view'),
    path('genre/delete/<int:pk>', GenreDelete.as_view(),
         name='genre_delete_view'),
    path('publisher/delete/<int:pk>', PublisherDelete.as_view(),
         name='publisher_delete_view'),
]
