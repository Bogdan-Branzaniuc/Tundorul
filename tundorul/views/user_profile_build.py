from tundorul.models import UserProfile
from allauth.socialaccount.models import SocialAccount
from datetime import datetime
from allauth.socialaccount.signals import pre_social_login
from allauth.account.signals import user_logged_in
from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from allauth.socialaccount.models import SocialAccount, SocialToken
import requests
from django.shortcuts import render, get_object_or_404, reverse
import os
import json

def is_follower(extra_data, token):
    headers = {
        'Authorization': 'Bearer ' + f'{token}',
        'Client-Id': os.environ.get('CLIENT_ID'),
    }

    params = {
        'user_id': extra_data['id'],
    }
    url = 'https://api.twitch.tv/helix/channels/followed'
    following_streams_request = requests.get(url, headers=headers, params=params)
    following_streams = json.loads(following_streams_request.content.decode("utf-8"))['data']

    if following_streams:
        for followed in following_streams:
            if followed['broadcaster_login'] == 'tundorul':
                return True


@receiver(user_logged_in)
def update_user_profile(request, user, **kwargs):
    query_set_social = SocialAccount.objects.filter(user=request.user)
    sociallogin = get_object_or_404(query_set_social)
    query_set_token = SocialToken.objects.filter(account=sociallogin)
    token = get_object_or_404(query_set_token).token
    extra_data = sociallogin.extra_data

    is_following = is_follower(extra_data, token)

    if UserProfile.objects.filter(username=sociallogin.user).exists():

        instance = get_object_or_404(UserProfile.objects.filter(username=sociallogin.user))
        instance.username = sociallogin.user
        instance.uid = extra_data['id']
        instance.current_name = extra_data['display_name']
        instance.email = extra_data['email']
        instance.is_follower = is_following
        # is_subscribed = request
        instance.save()

    else:
        print('added')
        user_profile = UserProfile.objects.create(
            username=sociallogin.user,
            uid=extra_data['id'],
            current_name=extra_data['display_name'],
            email=extra_data['email'],
            is_follower=is_following
        )
        user_profile.save()



