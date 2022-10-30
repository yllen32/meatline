from decimal import Decimal

from django.shortcuts import get_object_or_404
from django.db.models import Sum

from .models import Card
from .validators import validate_card_quantity

def add_to_card(request_data, products, card_id):
    """
    Returns queryset of the new card after adding new items.

    request_data: dict - dictionary with data from form
    quantity: float - quantity of added products
    card_id: str - id of the card for adding new items
    """
    product_id = int(request_data.get('id_product'))
    quantity = float(request_data.get('slider_for_product'))
    validate_card_quantity(value=quantity)
    product = get_object_or_404(products, pk=product_id)        
    current_user_card, created = Card.objects.get_or_create(
        card_id = card_id,
        product = product,
    )
    current_user_card.quantity = quantity
    current_user_card.save()
    return Card.objects.filter(card_id = card_id)

def change_card(request_data, card_items):
    """"""
    id_for_delete = request_data.get('item_for_delete')
    id_for_change = request_data.get('item_for_change')
    quantity = request_data.get('quantity_for_change')
    if id_for_delete:
        product = get_object_or_404(card_items, id=int(id_for_delete))
        product.delete()
    if id_for_change:
        product = get_object_or_404(card_items, id=int(id_for_change))
        product.quantity = Decimal(quantity)
        product.save()
    return Card.objects.filter(card_id = product.card_id)

def get_card_info(key):
    """Get card details."""
    card = Card.objects.filter(card_id = key)
    total_price = (
        card.aggregate(total_price = Sum('price'))
        ).get('total_price') or 0
    return card, total_price

