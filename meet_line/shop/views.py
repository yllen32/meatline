from datetime import datetime
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView

from .models import Product, Card
from .card import add_to_card, change_card, get_card_info
from .forms import ShopRequestFrom

class AboutShop(TemplateView):
    """Staticview for about page."""
    template_name = 'shop/about.html'

class ContactShop(TemplateView):
    """Staticview for about page."""
    template_name = 'shop/contacts.html'

def shop(request):
    """Return products to main page and form for putting it in to card."""
    products = Product.objects.filter(is_available=True)
    if not request.session.session_key:
        # Create session by adding date of first join in to the site
        request.session['date_of_key'] = str(datetime.now())
    session_key = request.session.session_key
    card, total_price = get_card_info(session_key)
    if request.method == 'POST':
        card, total_price = add_to_card(
            request_data=request.POST,
            products=products,
            card_id=session_key
        )
    return render(request, 'shop/products.html', context = {
            'products':products,
            'card':card,
            'total_price': total_price
        },
    )

def card(request):
    """Return a list of card items"""
    card, total_price = get_card_info(request.session.session_key)
    if request.method == 'POST':
        card, total_price = change_card(
            request_data=request.POST, card_items=card
        )
    return render(request, 'shop/card.html', context={
        'card': card,
        'total_price': total_price
        }
    )

def request(request):
    """Return a form to making request."""
    form = ShopRequestFrom(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('shop:index' )
    return render(request, 'shop/request.html', context={'form': form})
