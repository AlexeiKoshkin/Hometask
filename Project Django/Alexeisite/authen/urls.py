from django.urls import path
from authen.models import *
from authen.views import *

urlpatterns = [

    path('login/', MyLoginView.as_view(),
         name='log_in'),
    path('logout/', MyLogoutView.as_view(),
         name='log_out'),
]
