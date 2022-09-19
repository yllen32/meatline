from django.shortcuts import render

from .models import Product

def index(request):
    """Return a main page of shop with products."""
    products = Product.objects.all()
    return render(
        request, 'shop/products.html', context = {'products':products},
    )

