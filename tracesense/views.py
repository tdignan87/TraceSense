from django.shortcuts import render
from checkout.models import Order



def main_page(request):
    """ A view to return the main home page """
    
    return render(request,"pages/index.html")

def support_page(request):
    """ A view to return the support page """
    return render(request,"pages/support.html")


def about_page(request):
    """ A view to return the about page """
    return render(request,"pages/about.html")

def pricing_page(request):
    """ A view to return the pricing page """
    order = Order.objects.get()
    context={'order':order}
    return render(request,"pages/pricing_page.html",context)

