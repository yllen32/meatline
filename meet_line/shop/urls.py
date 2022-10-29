from django.urls import path

from .views import shop, card, request, AboutShop

app_name = 'shop'

urlpatterns = [
    path('', shop, name='shop'),
    path('card', card, name='card'),
    path('request', request, name='request'),
    path('about', AboutShop.as_view(), name='about')
]
