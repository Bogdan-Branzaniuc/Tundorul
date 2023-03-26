from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View

from allauth.socialaccount.providers.twitch.views import TwitchOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.models import SocialAccount, SocialToken

class TwitchToken(View):
    def get(request):
        account = SocialAccount.objects.get(user=request.user, provider='twitch')
        print('account')
        adapter = TwitchOAuth2Adapter(request)
        client = OAuth2Client(adapter)
        token = client.get_access_token(account.token_url, data={'code': request.GET.get('code')})
        SocialToken.objects.get_or_create(account=account, token=token['access_token'])
        print('e voilla')
        return redirect('home')
