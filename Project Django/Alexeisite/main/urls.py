from django.urls import path
from main.views import *

urlpatterns = [
    path('', LastView.as_view(), name='last_list_view'),
]
