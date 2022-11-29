from django.contrib import admin

from .models import Item


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'price')


admin.site.register(Item, ProductAdmin)
