from django.urls import path
from purchase.views import purchase,purchase_success, cache_checkout_data,purchase_failure
from .webhooks import webhook

urlpatterns = [
    path('',purchase,name="purchase"),
    path('purchase/success/<order_number>',purchase_success, name="purchase_success"),
    path('purchase/failure/',purchase_failure, name="purchase_failure"),
    path('cache_checkout_data/',cache_checkout_data, name="cache_checkout_data"),
    path('wh/', webhook, name="webhook"),
]
