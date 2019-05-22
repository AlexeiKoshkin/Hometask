from django.urls import path
from order.models import *
from order.views import *

urlpatterns = [

    path('create', OrderCheckOutView.as_view(),
         name='order_create'),
    path('success/<int:pk>', OrderSuccessView.as_view(),
         name='order_success'),
]
