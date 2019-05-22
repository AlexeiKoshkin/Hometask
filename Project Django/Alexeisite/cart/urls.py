from django.urls import path
from cart.models import *
from cart.views import *

urlpatterns = [

    path('add/<int:pk>', AddBookToCart.as_view(),
         name='add_book_to_cart'),
    path('view/', CartView.as_view(),
         name='view_cart')
]
