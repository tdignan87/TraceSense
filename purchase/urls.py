from django.urls import path
from purchase.views import purchase,purchase_success

urlpatterns = [
    path('',purchase,name="purchase"),
    path('purchase/success/<order_number>',purchase_success, name="purchase_success"),
]
