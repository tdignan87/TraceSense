from django.shortcuts import render

def new_department(request):
    """ A view to return to the main home page """
    return render(request,"pages/new_department.html")