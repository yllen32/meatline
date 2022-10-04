from datetime import datetime
from django.shortcuts import get_object_or_404, render
from django.db.models import Sum

from .models import Product, Card
from .card import add_to_card, change_card

def index(request):
    """Return products to main page and form for putting it in to card."""
    products = Product.objects.all()
    if not request.session.session_key:
        # Create session by adding date of first join in to the site
        request.session['date_of_key'] = str(datetime.now())
    session_key = request.session.session_key
    card = Card.objects.filter(card_id = session_key)
    if request.method == 'POST':
        card = add_to_card(
            request_data=request.POST,
            products=products,
            card_id=session_key
        )
    return render(request, 'shop/products.html', context = {
            'products':products,
            'card':card
        },
    )

def card(request):
    """Return a list of card items"""
    card_items = Card.objects.filter(card_id=request.session.session_key)
    print(request.POST)
    if request.method == 'POST':
        card_items = change_card(
            request_data=request.POST, card_items=card_items
        )
    total_price = (
        card_items.aggregate(total_price = Sum('price'))
        ).get('total_price') or 0
    print(request.POST)
    return render(request, 'shop/card.html', context={
        'card_items': card_items,
        'total_price': total_price
        }
    )
