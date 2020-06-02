from django.urls import path
from purchase.views import purchase

urlpatterns = [
    path('',purchase,name="purchase")
]
