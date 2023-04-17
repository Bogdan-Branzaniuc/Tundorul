from Tundorul.views import home, vods, giveaway, set_schedule
from Tundorul.views import set_schedule
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path('', home.Home.as_view(), name='home'),
    path('vods', vods.HandleVods.as_view(), name='vods'),
    path('giveaway', giveaway.Giveaway.as_view(), name='giveaway'),
]
