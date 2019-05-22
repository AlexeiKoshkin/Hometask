from django.contrib import admin

# Register your models here.
from . import models


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')


class SerieAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


class OrderStatusAdmin(admin.ModelAdmin):
    list_display = ('status_type',)
    search_fields = ('status_type',)


admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Serie, SerieAdmin)
admin.site.register(models.Genre, GenreAdmin)
admin.site.register(models.Publisher, PublisherAdmin)
admin.site.register(models.OrderStatus, OrderStatusAdmin)
