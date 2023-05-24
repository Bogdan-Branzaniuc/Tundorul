from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from tundorul.models import Vods, UserProfile

from django.http import HttpResponseRedirect
from django.contrib import messages
from allauth.socialaccount.models import SocialToken, SocialAccount
import requests
import json



class HandleVods(View):
    def get(self, request, *args, **kwargs):
        user_profile = []
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