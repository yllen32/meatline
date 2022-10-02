from decimal import Decimal

from django.shortcuts import get_object_or_404

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
