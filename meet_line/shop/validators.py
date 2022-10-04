from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

phone_validator = RegexValidator(
    regex=r'/(?:\+|\d)[\d\-\(\) ]{9,}\d/g',
    message="Введите номер мобильного телефона"
    )

def validate_card_quantity(value):
    """Валидация колличества продукта перед добавлением в корзину."""
    if not (value < 10 and value > 0):
        raise ValidationError(
            f'Неверное колличестов добовляемого продукта {value}'
        )
