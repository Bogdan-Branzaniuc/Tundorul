from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from .models import UserProfile
from allauth.socialaccount.models import SocialAccount
from datetime import datetime


class PopulateUserProfile(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            'index.html',
            {}
        )


