from django.urls import path
from profiles.views import profile_page

urlpatterns = [
    path('',profile_page,name="dashboard"),
]