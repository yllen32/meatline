from django.db.models import (Model, CharField, TextField, DecimalField, ImageField)
from django.contrib.auth import get_user_model

User = get_user_model()


class Product(Model):
    name = CharField(max_length=50, verbose_name='Название товара')
    price = DecimalField(verbose_name='Цена', max_digits=6, decimal_places=2)
    description = TextField(verbose_name='Описание товара')
    picture_url = ImageField(
        verbose_name='Фото товара',
        max_length=100,
        upload_to = 'images/'
    )

    def __str__(self):
        return self.name