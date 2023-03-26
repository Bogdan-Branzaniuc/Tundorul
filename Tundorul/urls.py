from Tundorul.views import home, twitch
from django.urls import path

urlpatterns = [
    path('', home.Home.as_view(), name='home'),
    path('accounts/twitch/login/callback/', twitch.TwitchToken.as_view(), name='twitch'),
]
