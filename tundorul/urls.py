from tundorul.views import home, vods, user_profile, pending_approval, banned_user
from django.urls import path, include

urlpatterns = [
    path("accounts", include("allauth.urls")),
    path('', home.Home.as_view(), name='home'),
    path('vods', vods.HandleVods.as_view(), name='vods'),
    path('user_profile', user_profile.UserProfileView.as_view(), name='user_profile'),
    path('pending_approval', pending_approval.PendingApproval.as_view(), name='pending_approval'),
    path('banned_user', banned_user.BannedUser.as_view(), name='banned_user'),
]

