from decimal import Decimal
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()


class Product(models.Model):

    AMOUNT_CHOICES = [
        ('kg', 'кг'),
        ('pcs', 'шт')
    ]

    name = models.CharField(max_length=50, verbose_name='Название товара')
    price = models.DecimalField(verbose_name='Цена', max_digits=6, decimal_places=2)
    description = models.TextField(verbose_name='Описание товара')
    picture_url = models.ImageField(
        verbose_name='Фото товара',
        max_length=100,
        upload_to = 'images/'
    )
    amount = models.CharField(
        choices=AMOUNT_CHOICES,
        max_length = 3,
        default = 'kg',
        verbose_name = 'Мера (кг или шт)'
        )
    

    def __str__(self):
        return self.name

class Card(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Товар',
        null=True,
    )
    quantity = models.IntegerField(
        verbose_name='Колличество',
        validators=[
            MinValueValidator(1),
            MaxValueValidator(10)
        ],
        null=True,
    )
    price = models.DecimalField(
        max_digits=10,
        blank=True,
        decimal_places=2,
        verbose_name='Цена',
        null=True,
    )
    card_id = models.CharField(
        max_length=40,
        verbose_name='Идентификатор корзины'
        )

    