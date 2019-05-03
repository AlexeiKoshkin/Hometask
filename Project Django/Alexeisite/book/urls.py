from django.urls import path
from book.models import *
from book.views import *

urlpatterns = [

    path('<int:pk>', BookDetail.as_view(),
         name='book_detail_view'),
    path('', BookList.as_view(),
         name='book_list_view'),
    path('create/', BookCreate.as_view(),
         name='book_create_view'),
    path('update/<int:pk>', BookUpdate.as_view(),
         name='book_update_view'),
    path('delete/<int:pk>', BookDelete.as_view(),
         name='book_delete_view'),
]
