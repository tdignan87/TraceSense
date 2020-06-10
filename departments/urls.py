from django.urls import path
from departments.views import create_department,department_list,update_department

urlpatterns = [
  path("departments/",create_department,name="create_department"),
  path("view_departments/",department_list,name="list_departments"),
  path("update_department/<str:pk>",update_department,name="update_department"),
  
]