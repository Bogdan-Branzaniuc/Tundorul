from tundorul.models import UserProfile

from datetime import datetime
from allauth.account.signals import user_logged_in
from django.dispatch import receiver
from allauth.socialaccount.models import SocialAccount, SocialToken
import requests
from django.shortcuts import get_object_or_404
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
    following = False
    followed_at = '0000-00-00'
    if following_streams:
        for followed in following_streams:
            print(followed)
            if followed['broadcaster_login'] == 'tundorul':
                following = True
                followed_date = datetime.strptime(followed['followed_at'], '%Y-%m-%dT%H:%M:%SZ')
                followed_at = followed_date.strftime('%Y-%m-%d')
            else:
                continue
    else:
        following = False

    return {
        'is_following': following,
        'followed_at': followed_at,
    }

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
        instance.profile_picture_url = extra_data['profile_image_url']
        instance.join_date = is_following['followed_at']
        instance.is_follower = is_following['is_following']
        instance.save()
    else:
        user_profile = UserProfile.objects.create(
            username=sociallogin.user,
            uid=extra_data['id'],
            current_name=extra_data['display_name'],
            email=extra_data['email'],
            is_follower=is_following['is_following'],
            profile_picture_url=extra_data['profile_image_url'],
            join_date=is_following['followed_at'],
        )
        user_profile.save()
