from tundorul.views import home, vods, user_profile, suggestions
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path("accounts", include("allauth.urls")),
    path('', home.Home.as_view(), name='home'),
    path('vods', vods.HandleVods.as_view(), name='vods'),
    path('user_profile', user_profile.UserProfileView.as_view(), name='user_profile'),
    path('suggestions', suggestions.Suggestions.as_view(), name='suggestions'),
]
