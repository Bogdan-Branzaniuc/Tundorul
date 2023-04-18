from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from allauth.socialaccount.models import SocialToken, SocialAccount
import requests

import requests

class HandleVods(View):
    def get(self, request, *args, **kwargs):
        """
        this view will send a request to the api for The last VODS to be displaied in the home-page
        """
        query_set1 = SocialAccount.objects.filter(user=request.user)
        social_user = get_object_or_404(query_set1)
        query_set2 = SocialToken.objects.filter(account=social_user)
        social_user_token = get_object_or_404(query_set2).token
        print(social_user_token)

        headers = {
                    'Authorization': 'Bearer ' + social_user_token,
                    'Client-Id': 'hf3ftyp7rubp7kdu4ebr7fy0flzba8',
                   }
        params = {
            'game_id': '499856',
            'period': 'month',
            'first': '100',
        }
        url = 'https://api.twitch.tv/helix/videos'

        ############ ***This works good enough for the current state and needs to be wired with the real account and model***
        # result = requests.get(url, headers=headers, params=params)
        # data = result.json()
        #
        # for field in data['data']:
        #     if field['user_name'] == 'tundorul':
        #         print(field)
        #
        #
        return render(
            request,
            'vods.html',
        )