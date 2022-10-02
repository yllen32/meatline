from django.urls import path

from .views import index, card

app_name = 'shop'

urlpatterns = [
    path('', index, name='index'),
    path('card/', card, name='card'),
]
