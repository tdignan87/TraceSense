from django.urls import path, include
from profiles.views import profile_page

urlpatterns = [
    path('',profile_page,name="dashboard"),
]