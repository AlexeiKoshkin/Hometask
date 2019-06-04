from django.urls import path
from order.models import *
from order.views import *

urlpatterns = [

    path('create', OrderCheckOutView.as_view(),
         name='order_create'),
    path('success/<int:pk>', OrderSuccessView.as_view(),
         name='order_success'),
    path('list', OrderListView.as_view(),
         name='order_list'),
    path('update/<int:pk>', OrderUpdateView.as_view(),
         name='order_update'),
    path('canceled/<int:pk>', OrderCanceledView.as_view(),
         name='order_canceled'),
]
