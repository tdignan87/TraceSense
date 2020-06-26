from django.shortcuts import render


def profile_page(request):
   
    return render(request,"pages/dashboard.html")

def change_password(request):
    return render(request,"allauth/account/password_change.html")

def reset_password(request):
    return render(request,"allauth/account/password_reset.html")