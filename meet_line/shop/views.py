from django.shortcuts import render

def index(request):
    """Return a main page."""
    return render(request, 'shop/products.html')

