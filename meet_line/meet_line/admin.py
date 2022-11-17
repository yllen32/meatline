from django.contrib import admin
from shop.models import Product, ShopRequest, Category


class MyAdminSite(admin.AdminSite):
    site_header = 'Мясной администратор'
    site_title = 'Мясной администратор'
    index_title = 'Управление магазином'

admin_site = MyAdminSite(name='admin')
admin_site.register([ShopRequest, Category])


