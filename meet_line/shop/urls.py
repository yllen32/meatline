from django.urls import path

from .views import index, card, request, AboutShop

app_name = 'shop'

urlpatterns = [
    path('', index, name='index'),
    path('card', card, name='card'),
    path('request', request, name='request'),
    path('about', AboutShop.as_view(), name='about')
]
