from django.shortcuts import render
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore

from .models import Product

def index(request):
    """Return a main page of shop with products."""
    products = Product.objects.all()
    if request.session.session_key == None:
        print('newuser')
        request.session['joins'] = '0'
    else:
        print('oldsession')
        ses = Session.objects.get(pk = request.session.session_key)
        data = ses.get_decoded()
        joins = data.get('joins')
        request.session['joins'] = str(int(joins)+1)
        print(ses.get_decoded())
    print(request.session.session_key)
    return render(
        request, 'shop/products.html', context = {'products':products},
    )
