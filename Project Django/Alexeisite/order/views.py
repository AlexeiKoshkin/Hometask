from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from .models import Order
from .forms import CheckOutOrderForm
from django.urls import reverse_lazy


class OrderCheckOutView(CreateView):
    model = Order
    template_name = 'cart/view_cart.html'
    form_class = CheckOutOrderForm

    def get_success_url(self):
        del self.request.session['cart_id']
        return reverse_lazy('order_success', kwargs={'pk': self.object.pk})


class OrderSuccessView(DetailView):
    model = Order
    template_name = 'order/order_success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object.cart.user.pk == self.request.user.pk:
            return context


class OrderListView(ListView):
    model = Order
    template_name = 'order/order_list.html'
    #permission_required = 'books.edit_order'


class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'order/order_update.html'
    fields = ['status']
    #permission_required = 'books.edit_order'

    def get_success_url(self):
        return reverse_lazy('order_list')


class OrderCanceledView(UpdateView):
    model = Order
    template_name = 'order/order_canceled.html'
    fields = ['canceled']

    def get_success_url(self):
        self.object.canceled = True
        self.object.save()
        return reverse_lazy('cart_user_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
