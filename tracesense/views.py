from django.shortcuts import render
from django.contrib.auth import user_logged_in


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
    return render(request,"pages/pricing_page.html")

