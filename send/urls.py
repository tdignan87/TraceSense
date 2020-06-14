from django.urls import path
from . import views
from .views import send_form,confirm_mail

urlpatterns = [
     path("send/",send_form,name="new_enquiry"),
     path("confirmation/",confirm_mail,name="confirmation_sent")
]