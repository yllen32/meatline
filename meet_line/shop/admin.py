from django.contrib import admin

from .models import Product, ShopRequest

@admin.register(Product, ShopRequest)
class ShopAdmin(admin.ModelAdmin):
    pass