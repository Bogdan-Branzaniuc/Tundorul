from Tundorul.views import home, vods
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path('', home.Home.as_view(), name='home'),
    path('/vods', vods.HandleVods.as_view(), name='vods'),
]
