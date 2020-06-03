from django.shortcuts import render
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm

import stripe

def purchase(request):
    
    total_price = OrderForm
    total = total_price['grand_total']
    stripe_total = round(total * 100)
    order_form = OrderForm()
    template = "pages/purchase.html"
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_DhfmGd6sRXHlrToC8LKDhm9G00cXBI34oU',
        'client_secret': 'test client secret',
    }
    
    return render(request,template,context)
