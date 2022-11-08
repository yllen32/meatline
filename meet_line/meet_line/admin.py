from django.contrib import admin
from shop.models import Product, ShopRequest, Category


class MyAdminSite(admin.AdminSite):
    site_header = 'Мясной администратор'

admin_site = MyAdminSite(name='admin')
admin_site.register([Product, ShopRequest, Category])