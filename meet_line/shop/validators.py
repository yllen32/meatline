from django.shortcuts import get_object_or_404
from .models import Card

from django.core.exceptions import ValidationError

def validate_card_quantity(quantity):
    """Валидация колличества продукта перед добавлением в корзину."""
    if not (quantity <= 10 and quantity > 0):
        raise ValidationError(
            f'Неверное колличестов добовляемого продукта {quantity}'
        )
