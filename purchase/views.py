from django.shortcuts import render
from django.contrib import messages

from .forms import OrderForm

def purchase(request):
    order_form = OrderForm()
    template = "pages/purchase.html"
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_DhfmGd6sRXHlrToC8LKDhm9G00cXBI34oU',
        'client_secret': 'test client secret',
    }
    
    return render(request,template,context)
