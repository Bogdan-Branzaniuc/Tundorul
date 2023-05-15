from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from tundorul.models import Vods

from django.http import HttpResponseRedirect
from django.contrib import messages
from allauth.socialaccount.models import SocialToken, SocialAccount
import requests
import json


class HandleVods(View):
    def get(self, request, *args, **kwargs):
        """

        """
        context = {
            'vods': Vods.objects.all()
        }

        return render(
            request,
            'vods.html',
            context,
        )