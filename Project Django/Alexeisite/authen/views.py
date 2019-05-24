from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView


class MyLoginView(LoginView):
    template_name = 'authen/login.html'


class MyLogoutView(LogoutView):
    extra_context = 'none'
