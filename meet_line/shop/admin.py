from django.contrib import admin

from .models import Product, ShopRequest, Category

@admin.register(Product, ShopRequest, Category)
class ShopAdmin(admin.ModelAdmin):
    pass
