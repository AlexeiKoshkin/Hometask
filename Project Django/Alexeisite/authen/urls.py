from django.urls import path
from authen.models import *
from authen.views import *

urlpatterns = [

    path('login/', MyLoginView.as_view(),
         name='log_in'),
    path('logout/', MyLogoutView.as_view(),
         name='log_out'),
    path('create_user/', CreateUserView.as_view(),
         name='create_user'),
    path('update_user/<int:pk>', UpdateUserView.as_view(),
         name='update_user'),
    path('view_user/<int:pk>', ViewUserView.as_view(),
         name='view_user'),  
]
