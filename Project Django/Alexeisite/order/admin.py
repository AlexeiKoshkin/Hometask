from django.contrib import admin
from .import models


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'cart',
        'status',
        'delivery_address',
        'email',
        'phone',
        'comments'
    )
    list_filter = ('cart',)


admin.site.register(models.Order, OrderAdmin)
