from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
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
    template_name = 'order/success.html'
