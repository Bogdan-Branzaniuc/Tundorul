from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
import requests

class Home(View):
    def retrieveSchedule(self, request, *args, **kwargs):
        payload = {
            'client_id': '',
            'client_secret': '',
            'grant_type': 'client_credentials',
        }
        url = 'uri:https://id.twitch.tv/oauth2/token,'
        response = requests.post(url, data=payload)

    def get(self, request, *args, **kwargs):
        return render(
            request,
            'index.html',
        )

