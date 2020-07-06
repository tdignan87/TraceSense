from django.shortcuts import render,redirect
from checkout.forms import OrderForm
from checkout.models import Order
from django.conf import settings

import stripe

def checkout(request):
    """ A view for handling stripe payments purchasing products page."""
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    order = Order.objects.get()
    if request.method == 'POST':
        stripe_total = 200 * 100
        form = OrderForm(request.POST)
        if form.is_valid():
            createPayment = form.save(commit=False)
            createPayment.user_id = request.user.id
            form.save()
            return redirect(payment_success)         
    else:
        stripe_total = 200 * 100
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        
        checkoutForm = OrderForm()
        context = {'form':checkoutForm,
                'stripe_public_key': stripe_public_key,
                'client_secret': intent.client_secret,
                'order':order}
    return render(request,"checkout.html",context)

def payment_success(request):
    """ Handle successful payments"""
    save_info = request.session.get('save_info')
    
    return render(request,"success.html")



def payment_failure(request):
    return render("failure.html")
  