from django.shortcuts import render, reverse, redirect, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from purchase.models import Order

import stripe

@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid,metadata={
            'save_info':request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def purchase(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    
    if request.method == 'POST':
        
        form_data = {
            
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address': request.POST['street_address'],
           
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
           order = order_form.save()
           return redirect(reverse('purchase_success',args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. Please double check your information and try again.')
    else:
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

def purchase_success(request, order_number):
    """
    Handle successful payments
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order,order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
            email will be sent to {order.email}.')
    
    template = "pages/success.html"
    context = {
        'order': order,
    }
    
    return render(request, template, context)
