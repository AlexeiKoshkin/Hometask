from django.shortcuts import render
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from book.models import Book
from cart.models import BookInCart, Cart, User
from .forms import AddBookForm
from django.urls import reverse_lazy
from reference.models import OrderStatus
from order.forms import CheckOutOrderForm


new_order_status = OrderStatus.objects.get(pk=1)


class AddBookToCart(UpdateView):
    model = BookInCart
    form_class = AddBookForm
    template_name = 'cart/add_book.html'

    def get_object(self, queryset=None):
        cart_id = self.request.session.get('cart_id')
        if self.request.user.is_anonymous:
            user = None
        else:
            user = self.request.user
        cart, created = Cart.objects.get_or_create(
            pk=cart_id,
            defaults={
                'user': user
            }
        )
        self.request.session['cart_id'] = cart.pk
        book_pk = self.kwargs.get('pk')
        book = Book.objects.get(pk=book_pk)
        book_in_cart, created = self.model.objects.get_or_create(
            cart=cart,
            book=book,
            defaults={
                'quantity': 1
            }
        )
        if not created:
            book_in_cart.quantity += 1
        return book_in_cart

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_id'] = self.kwargs.get('pk')
        context['next'] = self.request.GET.get('next', '/')
        return context

    def get_success_url(self):
        return self.request.POST.get('next', '/')


class CartView(DetailView):
    model = Cart
    template_name = 'cart/view_cart.html'

    def get_object(self, queryset=None):
        cart_id = self.request.session.get('cart_id')
        if self.request.user.is_anonymous:
            user = None
        else:
            user = self.request.user
        cart, created = Cart.objects.get_or_create(
            pk=cart_id,
            defaults={
                'user': user
            }
        )
        return cart

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        checkout_form = CheckOutOrderForm()
        checkout_form.fields['cart'].initial = self.object
        checkout_form.fields['status'].initial = new_order_status
        context['form'] = checkout_form
        return context


class DeleteBookFromCart(DeleteView):
    model = BookInCart
    template_name = 'cart/delete_book.html'

    def get_success_url(self):
        return reverse_lazy('view_cart')


class OrderUserListView(ListView):
    model = Cart
    template_name = 'cart/order_user_list.html'
    login_url = '/authen/login'

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        current_user = self.request.user
        return qs.filter(user=current_user)
