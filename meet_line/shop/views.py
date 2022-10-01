from datetime import datetime
from django.shortcuts import render

from .models import Product, Card
from .card import add_to_card

def index(request):
    """Вернуть список продуктов и продукты текущей страницы для index."""
    products = Product.objects.all()
    if not request.session.session_key:
        # инициируем сессию за счет добавления в куки даты первого sessionkey
        request.session['date_of_key'] = str(datetime.now())
    session_key = request.session.session_key
    card = Card.objects.filter(card_id = request.session.session_key)
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
    """Вернуть список товаров в корзине."""
    