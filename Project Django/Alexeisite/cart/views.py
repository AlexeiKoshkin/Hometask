from django.views.generic.edit import UpdateView
from django.views.generic import TemplateView
from book.models import Book
from cart.models import BookInCart, Cart
from .forms import AddBookForm
from django.urls import reverse_lazy


class AddBookToCart(UpdateView):
    model = BookInCart
    form_class = AddBookForm
    template_name = 'cart/add_book.html'

    def get_object(self, queryset=None):
        cart_id = self.request.session.get('cart_id')
        cart, created = Cart.objects.get_or_create(
            pk=cart_id,
            defaults={
                'user': self.request.user
            }
        )
        self.request.session['cart_id'] = cart.pk
        book_pk = self.kwargs.get('pk')
        print(book_pk, 'fddddddddddddddddd')
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
        return context
