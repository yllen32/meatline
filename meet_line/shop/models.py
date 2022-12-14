from decimal import Decimal

from django.db import models
from django.contrib.auth import get_user_model

from PIL import Image

from .validators import validate_card_quantity, phone_validator

User = get_user_model()


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Категория товара",
    )
    slug = models.SlugField(verbose_name="Имя для url")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории товаров'


class Product(models.Model):

    AMOUNT_CHOICES = [
        ('kg', 'кг'),
        ('pcs', 'шт')
    ]
    name = models.CharField(max_length=50, verbose_name='Название товара')
    price = models.DecimalField(
        verbose_name='Цена', max_digits=6, decimal_places=2
    )
    description = models.TextField(
        verbose_name='Описание товара', blank=True, null=True
    )
    picture_url = models.ImageField(
        verbose_name='Фото товара',
        max_length=100,
        upload_to='images/'
    )
    amount = models.CharField(
        choices=AMOUNT_CHOICES,
        max_length=3,
        default='kg',
        verbose_name='Мера (кг или шт)'
        )
    is_available = models.BooleanField(
        default=True,
        verbose_name="Товар доступен?"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория к которой относится товар.",
        null=True,
        related_name="products"
    )

    def __str__(self):
        return self.name
    
    def save(self):
        super().save()
        image_path = self.picture_url.path
        img = Image.open(image_path)
        if img.height>900 or img.width > 900:
            img.thumbnail((600, 600))
            img.save(image_path)


    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


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
        self.price = Decimal(self.quantity or 1)*self.product.price
        super(Card, self).save(*args, **kwargs)

    def __str__(self):
        """Return a string with necessary request info."""
        data = (
            self.product,
            self.quantity,
            self.product.get_amount_display(),
            self.price,
        )
        request_info = ''
        for item in data:
            request_info += str(item) + ' '
        return request_info

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
    """Model for storage cards info. """
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
        validators=[phone_validator, ],
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
    request_date = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата заявки',
        null=True,
    )

    def __str__(self):
        data = (
            self.name,
            self.phone,
            self.address,
            self.comment,
        )
        consumer_info = ''
        for item in data:
            consumer_info += str(item) + '\n'
        return consumer_info

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
