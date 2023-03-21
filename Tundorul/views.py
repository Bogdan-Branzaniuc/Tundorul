from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse
from django.views import View
import requests


class MyView(View):

    def get(self, request, *args, **kwargs):
        template_name = 'index.html'
        return render(
            request,
            'index.html',
            {}
        )
        return HttpResponse('')


    def exchange_code_for_token(request):
        code = request.GET.get('code')
        redirect_uri = 'http://localhost:8000/accounts/twitch/login/callback/'
        payload = {
            'client_id': '<your-client-id>',
            'client_secret': '<your-client-secret>',
            'code': code,
            'grant_type': 'authorization_code',
            'redirect_uri': redirect_uri,
        }
        response = requests.post('https://id.twitch.tv/oauth2/token', data=payload)
        access_token = response.json()['access_token']
        # Save the access token to the user's account or session