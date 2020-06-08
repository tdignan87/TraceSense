from django.urls import path
from audit.views import new_department

urlpatterns = [
    path('new/',new_department,name="new_department"),
    
]

