from tundorul.views import home, vods, user_profile, pending_approval, banned_user
from django.urls import path, include
from tundorul.views.handler_error_page import handler403,  handler404, handler405, handler500

urlpatterns = [
    path("accounts", include("allauth.urls")),
    path('', home.Home.as_view(), name='home'),
    path('vods', vods.HandleVods.as_view(), name='vods'),
    path('user_profile', user_profile.UserProfileView.as_view(), name='user_profile'),
    path('pending_approval', pending_approval.PendingApproval.as_view(), name='pending_approval'),
    path('banned_user', banned_user.BannedUser.as_view(), name='banned_user'),
]

handler403 = 'tundorul.views.handler_error_page.handler403'
handler404 = 'tundorul.views.handler_error_page.handler404'
handler405 = 'tundorul.views.handler_error_page.handler405'
handler500 = 'tundorul.views.handler_error_page.handler500'

