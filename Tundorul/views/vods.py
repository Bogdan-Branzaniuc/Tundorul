from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from allauth.socialaccount.models import SocialToken, SocialAccount
import requests

import requests


class HandleVods(View):
    def get(self, request, *args, **kwargs):
        #retrieve vods from twitch.

        query_set1 = SocialAccount.objects.filter(user=request.user)
        social_user = get_object_or_404(query_set1)
        query_set2 = SocialToken.objects.filter(account=social_user)
        social_user_token = get_object_or_404(query_set2).token
        print(social_user_token)

        headers = {'Authorisation': 'Bearer ' + f'social_user_token'}
        data = {
            'authorization': 'Bearer ' + social_user_token,
            'client_id': 'hf3ftyp7rubp7kdu4ebr7fy0flzba8',
            'user_id': '753993152',
        }
        url = 'https://api.twitch.tv/helix/videos'
        result = requests.get(url, data=data, headers=headers)
        print(headers)
        return render(
            request,

            'vods.html',
        )