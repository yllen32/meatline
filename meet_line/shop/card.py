from decimal import Decimal

from django.shortcuts import get_object_or_404

from .models import Card
from .validators import validate_card_quantity

def add_to_card(request_data, products, card_id):
    """
    Возвращает queryset новой корзины после добавления в неё новых продуктов.

    request_data: dict - словарь c информацией от формы продукта
    quantity: float - колличество добовляемого продукта в корзину
    card_id: str - id корзины в которую добовляется товар.
    """
    product_id = int(request_data.get('id_product'))
    quantity = float(request_data.get('slider_for_product'))
    validate_card_quantity(quantity=quantity)
    product = get_object_or_404(products, pk=product_id)        
    current_user_card, created = Card.objects.get_or_create(
        card_id = card_id,
        product = product,
    )
    current_user_card.quantity = quantity
    current_user_card.price = Decimal(quantity) * product.price
    current_user_card.save()
    return Card.objects.filter(card_id = card_id)
