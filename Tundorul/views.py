from django.http import HttpResponse
from django.views import View
import requests
from django.shortcuts import render, get_object_or_404, reverse
from django import forms
from .models import UserProfile
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import User
from datetime import datetime
from allauth.socialaccount.signals import pre_social_login, social_account_updated
from django.dispatch import receiver

@receiver(pre_social_login)
def signal_pre_social_login(sender, request, sociallogin, **kwargs):
    userInstance = get_object_or_404(User, username=sociallogin.account.user)
    #print(userInstance.__dir__())
    if UserProfile.objects.filter(username=sociallogin.account.user).exists():
        print("record here")
    else:
        print("SOCIAL ACCOUNT missing!!!!!!!!!!!!!!")
        print("SOCIAL ACCOUNT ADDED!!!!!!!!!!!!!!")
        print(sociallogin.account.extra_data)
        user_profile = UserProfile.objects.create(
            username=sociallogin.account.user,
            uid=sociallogin.account.extra_data['id'],
            current_name=sociallogin.account.extra_data['display_name'],
            email=userInstance.email,
            join_date=datetime.strptime('2000/10/06', '%Y/%m/%d'),
            time_watched=datetime(2000, 10, 20),
            channel_points=150,
            is_subscribed=True,
            subscribed_since=datetime(2000, 10, 20),
        )
        user_profile.save()


@receiver(social_account_updated)
def signal_social_account_updated(sender, request, sociallogin, **kwargs):
    userInstance = get_object_or_404(User, username=sociallogin.account.user)
    print(type(int(sociallogin.account.uid)))
    # here, update everything that changed in the records.

class PopulateUserProfile(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'index.html',
            {}
        )
        return HttpResponse('')



