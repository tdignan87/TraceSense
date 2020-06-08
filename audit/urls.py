from django.urls import path
from audit.views import new_department,update_department,department_list

urlpatterns = [
    path('new/',new_department,name="new_department"),
    path('update/<str:pk>',update_department,name="update_department"),
    path('edit/',department_list,name="department_list"),
]