from django.shortcuts import render
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm

import stripe

def purchase(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    
    total_price = 200
    stripe_total = total_price
    stripe.api_key = stripe_secret_key
    stripe.PaymentIntent.create(
       amount=stripe_total,
       currency=settings.STRIPE_CURRENCY, 
    )
    
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. Did you forget to set it?')
    
    
    order_form = OrderForm()
    template = "pages/purchase.html"
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': stripe_secret_key,
    }
    
    return render(request,template,context)
