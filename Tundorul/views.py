from django.http import HttpResponse
from django.views import View
import requests
from django.shortcuts import render, get_object_or_404, reverse
from django import forms
from .models import UserProfile
from allauth.socialaccount.models import SocialAccount
from datetime import datetime

class PopulateUserProfile(View):


    def get(self, request, *args, **kwargs):
        account = get_object_or_404(SocialAccount, uid=753993152)
        user_profile = UserProfile.objects.create(
            username=account.user,
            uid=account.extra_data['id'],
            current_name=account.extra_data['display_name'],
            email=account.extra_data['email'],
            join_date=datetime.strptime('2000/10/06', '%Y/%m/%d'),
            time_watched=datetime(2000, 10, 20),
            channel_points=150,
            is_subscribed=True,
            subscribed_since=datetime(2000, 10, 20),
        )
        user_profile.save()
        return render(
            request,
            'index.html',
            {}
        )
        return HttpResponse('')



