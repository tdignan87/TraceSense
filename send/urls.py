from django.urls import path
from . import views
from .views import send_form

urlpatterns = [
     path("send/",send_form,name="new_enquiry"),
     path("confirmation/",send_form,name="confirmation_sent")
]