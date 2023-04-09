from Tundorul.views import home
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path('', home.Home.as_view(), name='home'),
]
