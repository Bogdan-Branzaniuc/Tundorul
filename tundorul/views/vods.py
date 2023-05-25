from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from tundorul.models import Vods, UserProfile


class HandleVods(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user_profile = get_object_or_404(UserProfile, username=request.user)
            if user_profile.is_banned is True:
                return redirect('banned_user')

        context = {
            'vods': Vods.objects.all()
        }

        return render(
            request,
            'vods.html',
            context,
        )
