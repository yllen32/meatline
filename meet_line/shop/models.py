from django.db.models import (
    Model, CharField, TextField, ImageField, DecimalField
)
from django.contrib.auth import get_user_model

User = get_user_model()


class Product(Model):
    name = CharField(max_length=50, verbose_name='Название товара')
    price = DecimalField(verbose_name='Цена', max_digits=6, decimal_places=2)
    descroption = TextField(verbose_name='Описание товара')
    picture_url = CharField(verbose_name='Фото товара', max_length=100)
