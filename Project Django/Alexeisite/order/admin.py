from django.contrib import admin
from .import models


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'cart',
        'status',
        'canceled',
        'delivery_address',
        'email',
        'phone',
        'comments',
        'created_day',
        'updated_date'
    )
    list_filter = ('cart', 'status')

admin.site.register(models.Order, OrderAdmin)
