from django.urls import path
from purchase.views import purchase,purchase_success
from .webhooks import webhook

urlpatterns = [
    path('',purchase,name="purchase"),
    path('purchase/success/<order_number>',purchase_success, name="purchase_success"),
    path('wh/', webhook, name="webhook"),
]
