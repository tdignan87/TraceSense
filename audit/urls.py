from django.urls import path
from audit.views import new_audit

urlpatterns = [
  path("questions/",new_audit,name="new_audit"),
 
]