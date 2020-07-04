from django.shortcuts import render
from django.contrib.auth import user_logged_in


def profile_page(request):
   """ renders dashboard page showing information and menu items to user."""
   return render(request,"dashboard.html")

def change_password(request):
    return render(request,"allauth/account/password_change.html")

def reset_password(request):
    return render(request,"allauth/account/password_reset.html")