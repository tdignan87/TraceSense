"""tracesense URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from tracesense.views import main_page, support_page, about_page
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',main_page, name="main"),
    path("support/",support_page, name="support"),
    path("send/", include("send.urls")),
    path("about/",about_page, name="about"),
    path("accounts/", include("allauth.urls")),
    path("purchase/",include("purchase.urls")),
    path("profile/",include("profiles.urls")),
    path("areas/",include("areas.urls")),
     path("departments/",include("departments.urls")),
]
 
 
 
 
