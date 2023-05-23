from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from tundorul.models import UserProfile
from django.http import HttpResponseRedirect
from django.contrib import messages
import requests
from datetime import datetime


class UserProfileView(View):
    def get(self, request, *args, **kwargs):
        user_profile = get_object_or_404(UserProfile, username=request.user)
        if(request.user.is_authenticated):
            if user_profile.is_banned is True:
                return redirect('banned_user')
            user_data = {
                'username': user_profile.username,
                'current_name': user_profile.current_name,
                'email': user_profile.email,
                'join_date': user_profile.join_date.strftime("%d - %m - %Y"),
                'profile_picture_url': user_profile.profile_picture_url,
                'is_follower': user_profile.is_follower,
                'is_banned': user_profile.is_banned,
            }
            context = {
                'user_profile': user_data,
            }
        else:
            context = {}
        return render(
            request,
            'user_profile.html',
            context,
        )