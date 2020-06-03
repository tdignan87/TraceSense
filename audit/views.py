from django.shortcuts import render

def config(request):
    """ A view to return the main home page """
    return render(request,"pages/config.html")

