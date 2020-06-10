from django.urls import path
from areas.views import create_area,area_list,update_area,delete_area

urlpatterns = [
    path("area/",create_area,name="create_area"),
    path("area_list/",area_list,name="area_list"),
    path("update_area/<str:pk>",update_area,name="update_area"),
    path("delete_area/<str:pk>",delete_area,name="delete_area"),
]