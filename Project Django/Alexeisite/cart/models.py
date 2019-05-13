from django.db import models
from django.contrib.auth import get_user_model
from book.models import Book

User = get_user_model()


class Cart(models.Model):
    user = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.PROTECT
    )
    created_date = models.DateTimeField(
        "Дата создания корзины",
        auto_now=False,
        auto_now_add=True
    )
    update_date = models.DateTimeField(
        "Дата изменения",
        auto_now=True,
        auto_now_add=False
    )

    def __str__(self):
        return "Корзина"

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"


class BookInCart(models.Model):
    cart = models.ForeignKey(
        Cart,
        verbose_name="Книга в корзине",
        related_name="books_in_cart",
        on_delete=models.CASCADE
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE
    )
    quantity = models.IntegerField(
        "Количество"
    )
    created_date = models.DateTimeField(
        "Дата создания корзины",
        auto_now=False,
        auto_now_add=True
    )
    update_date = models.DateTimeField(
        "Дата изменения",
        auto_now=True,
        auto_now_add=False
    )

    def __str__(self):
        return "Товары в корзине"

    class Meta:
        verbose_name = "Книга в корзине"
        verbose_name_plural = "Книги в корзине"
        unique_together = (
            ('cart', 'book')
        )
