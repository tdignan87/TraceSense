from django.shortcuts import render
from checkout.models import Order



def profile_page(request):
   """ renders dashboard page showing information and menu items to user."""
   has_paid = Order.objects.filter(user_id=request.user.id)
   

   
   context = {'order':has_paid}
   print(context)
    
   return render(request,"dashboard.html",context)

def change_password(request):
    return render(request,"allauth/account/password_change.html")

def reset_password(request):
    return render(request,"allauth/account/password_reset.html")