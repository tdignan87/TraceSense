from django.shortcuts import render

def main_page(request):
    """ A view to return the main home page """
    return render(request,"pages/index.html")

def support_page(request):
    """ A view to return the support page """
    return render(request,"pages/support.html")

def about_page(request):
    """ A view to return the about page """
    return render(request,"pages/about.html")
