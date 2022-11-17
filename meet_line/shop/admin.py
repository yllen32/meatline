from django.contrib import admin

from .models import Product, ShopRequest, Category

@admin.register(Category)
class ShopAdmin(admin.ModelAdmin):
    pass

@admin.register(ShopRequest)
class RequestAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    readonly_fields = ('card_id', 'name', 'address', 'comment', 'phone')
    

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_per_page = 20
    search_fields = ('name',)
    list_filter = ('category',)
