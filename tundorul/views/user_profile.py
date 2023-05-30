from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import View
from tundorul.models import UserProfile


class UserProfileView(View):
    def get(self, request, *args, **kwargs):
        user_profile = []
        if request.user.is_authenticated:
            user_profile = get_object_or_404(UserProfile, username=request.user)
        if request.user.is_authenticated:
            if user_profile.is_banned is True:
                return redirect('banned_user')
            context = {
                'user_profile': user_profile,
            }
            return render(
                request,
                'user_profile.html',
                context,
            )
        else:
            return render(request, 'login_if_not.html', {'page': 'Profile'})
