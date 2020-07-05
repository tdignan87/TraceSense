from django.urls import path, include
from profiles.views import change_password,reset_password
from dashboard.views import profile_page

urlpatterns = [
    path("",profile_page,name="profile_page"),
    path("password/change/",change_password,name="change_password"),
    path("password/reset/",reset_password,name="reset_password"),
]