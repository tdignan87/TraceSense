from django.urls import path, include
from dashboard.views import profile_page,change_password,reset_password

urlpatterns = [
    path("",profile_page,name="dashboard"),
    path("password/change/",change_password,name="change_password"),
    path("password/reset/",reset_password,name="reset_password"),
]