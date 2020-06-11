from django.shortcuts import render,redirect
from .models import Transactions


def new_audit(request):
    """ A view to return the page for creating a new audit. """
    return render(request,"pages/new_audit.html")