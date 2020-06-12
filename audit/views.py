from django.shortcuts import render,redirect
from .models import Transactions


def new_audit(request):
    """ Create new audit and store into the database. This is just a test"""
    return render(request,"pages/new_audit.html")
