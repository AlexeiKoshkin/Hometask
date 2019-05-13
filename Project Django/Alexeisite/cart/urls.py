from django.urls import path
from cart.models import *
from cart.views import *

urlpatterns = [

    path('<int:pk>', AddBookToCart.as_view(),
         name='add_book_to_cart'),
]
