from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from cart.models import User
from django.urls import reverse_lazy
from .forms import CreateUserForm, UpdateUserForm


class MyLoginView(LoginView):
    template_name = 'authen/login.html'


class MyLogoutView(LogoutView):
    extra_context = 'none'


class CreateUserView(CreateView):
    model = User
    template_name = 'authen/create_user.html'
    form_class = CreateUserForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next', '/')
        return context

    def get_success_url(self):
        self.object.set_password(self.object.password)
        self.object.save()
        return self.request.POST.get('next', '/')


class UpdateUserView(UpdateView):
    model = User
    template_name = "authen/update_user.html"
    form_class = UpdateUserForm

    def get_success_url(self):
        print(self.object)
        return reverse_lazy('view_user', kwargs={'pk': self.object.pk})

    def test_func(self):
        return self.request.user.pk == self.kwargs.get('pk')


class ViewUserView(DetailView):
    model = User
    template_name = "authen/view_user.html"

    def test_func(self):
        return self.request.user.pk == self.kwargs.get('pk')

