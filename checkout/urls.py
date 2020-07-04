from django.urls import path
#from purchase.views import purchase,purchase_success, cache_checkout_data,purchase_failure
from checkout.views import checkout,payment_success,payment_failure



urlpatterns = [
    path('',checkout,name="checkout"),
    path('success',payment_success, name="payment_success"),
    path('failure/',payment_failure, name="purchase_failure"),
   # path('cache_checkout_data/',cache_checkout_data, name="cache_checkout_data"),
]
