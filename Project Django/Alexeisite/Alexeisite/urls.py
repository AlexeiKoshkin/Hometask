"""Alexeisite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from reference.models import *
from reference.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reference/author/<int:pk>', AuthorDetail.as_view(),
         name='author_detail_view'),
    path('reference/serie/<int:pk>', SerieDetail.as_view(),
         name='serie_detail_view'),
    path('reference/genre/<int:pk>', GenreDetail.as_view(),
         name='genre_detail_view'),
    path('reference/publisher/<int:pk>', PublisherDetail.as_view(),
         name='publisher_detail_view'),
    path('reference/author/', AuthorList.as_view(),
         name='author_list_view'),
    path('reference/serie/', SerieList.as_view(),
         name='serie_list_view'),
    path('reference/genre/', GenreList.as_view(),
         name='genre_list_view'),
    path('reference/publisher/', PublisherList.as_view(),
         name='publisher_list_view'),
    path('reference/', ReferenceVeiw.as_view()),
    path('main/', include('main.urls')),
    path('contacts/', include('contacts.urls')),
]
