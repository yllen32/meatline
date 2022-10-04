from decimal import Decimal
from email.policy import default
from tabnanny import verbose

from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator

from .validators import validate_card_quantity, phone_validator

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
    quantity = models.DecimalField(
        verbose_name='Колличество',
        validators=[validate_card_quantity],
        null=True,
        max_digits=3,
        decimal_places=1
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
    
    def save(self, *args, **kwargs):
        print(self.quantity)
        self.price = Decimal(self.quantity or 1)*self.product.price
        super(Card, self).save(*args, **kwargs)
        
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['product', 'card_id'],
                name='unique_card_product',
                violation_error_message=(
                    'Card can only have one instance of a product'
                )
            ),
        ]

class ShopRequest(models.Model):

    card_id = models.CharField(
        max_length=40,
        verbose_name='Идентификатор корзины'
        )
    name = models.CharField(
        max_length=30,
        verbose_name='Имя покупателя',
        help_text='Введите имя по которому к вам можно обращатся',
        blank=False
        )
    phone = models.CharField(
        validators=[phone_validator,],
        verbose_name='Номер телефона для связи',
        help_text='Введите номер вашего мобильного телефона',
        max_length=20
        )
    address = models.CharField(
        max_length=300,
        verbose_name="Адрес доставки",
        help_text="Введите адрес по которому доставить покупки" 
    )
    comment = models.TextField(
        max_length=300,
        verbose_name="Комментарий",
        help_text='Введите комментарий (если необходим)',
        null=True,
        blank=True,
    )
    is_delivered = models.BooleanField(
        default=False,
        verbose_name='Доставка выполнена?'
    )