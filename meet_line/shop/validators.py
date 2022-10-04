from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_card_quantity(value):
    """Валидация колличества продукта перед добавлением в корзину."""
    if not (value < 10 and value > 0):
        raise ValidationError(
            f'Неверное колличестов добовляемого продукта {value}'
        )
