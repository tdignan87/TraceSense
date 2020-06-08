from django.urls import path
from audit.views import new_department

urlpatterns = [
    path('new_department/',new_department,name="new_department"),
    
]

