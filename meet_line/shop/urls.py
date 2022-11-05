from django.urls import path

from .views import (
    shop, card, request, AboutShop, ContactShop, shop_redirect, DeliveryShop
)

app_name = 'shop'

urlpatterns = [
    path('shop', shop_redirect, name='shop_redirect'),
    path('shop/<str:category>', shop, name='shop'),
    path('card', card, name='card'),
    path('request', request, name='request'),
    path('', AboutShop.as_view(), name='about'),
    path('contacts', ContactShop.as_view(), name='contacts'),
    path('delivery', DeliveryShop.as_view(), name='delivery'),
]
