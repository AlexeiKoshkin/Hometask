from django.contrib import admin
from .import models


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name', 'price')


admin.site.register(models.Book, BookAdmin)
