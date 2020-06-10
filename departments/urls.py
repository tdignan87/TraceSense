from django.urls import path
from departments.views import create_department

urlpatterns = [
  path("departments/",create_department,name="create_department"),
]