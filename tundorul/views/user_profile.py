from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from tundorul.models import UserProfile
from django.http import HttpResponseRedirect
from django.contrib import messages
import requests
from datetime import datetime


class UserProfileView(View):
    def get(self, request, *args, **kwargs):
        if(request.user.is_authenticated):
            user_data = UserProfile.objects.filter(username=request.user)[0]
            print(user_data)
            user_data = {
                'username': user_data.username,
                'current_name': user_data.current_name,
                'email': user_data.email,
                'join_date': user_data.join_date.strftime("%d - %m - %Y"),
                'profile_picture_url': user_data.profile_picture_url,
                'is_follower': user_data.is_follower,
                'is_banned': user_data.is_banned,
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