from django.shortcuts import render
from django.contrib import messages

from .forms import OrderForm

def purchase(request):
    order_form = OrderForm()
    template = "pages/purchase.html"
    context = {
        'order_form': order_form,
    }
    
    return render(request,template,context)
