from django.db import models
from django.contrib.auth import get_user_model
from cart.models import Cart
from reference.models import OrderStatus


class Order(models.Model):
    cart = models.ForeignKey(
        Cart,
        verbose_name="Корзина",
        on_delete=models.PROTECT
    )
    status = models.ForeignKey(
        OrderStatus,
        verbose_name="Статус заказа",
        on_delete=models.PROTECT
    )
    delivery_address = models.TextField(
        "Адрес доставки",
        null=True,
        blank=True,
        help_text="Минск, ул. Первая, 7-77"
    )
    email = models.EmailField(
        verbose_name="Электронная почта",
        null=True,
        blank=True,
        help_text="user@gmail.com"
    )
    phone = models.CharField(
        verbose_name="Контактный телефон",
        help_text="+375-29-111-11-11",
        max_length=17
    )
    comments = models.TextField(
        verbose_name="Дополнительная информация",
        null=True,
        blank=True,
    )
    created_day = models.DateTimeField(
        "Дата внесения в корзину",
        auto_now=False,
        auto_now_add=True)

    updated_date = models.DateTimeField(
        "Дата последнего изменения",
        auto_now=True,
        auto_now_add=False)

    def __str__(self):
        return "Заказ № {}".format(self.cart.pk)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
