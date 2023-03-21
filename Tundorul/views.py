from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse
from django.views import View
import requests
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.shortcuts import render, get_object_or_404, reverse
from django import forms

class PopulateUser(View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            'index.html',
            {}
        )
        return HttpResponse('')


class SocialUserAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):
        user = super().save_user(request, sociallogin, form=None)
        if not user.is_staff:
            extra_data = sociallogin.account.extra_data
            user.id = extra_data['id']
            user.username = extra_data['login']
            user.email = extra_data['email']
            user.profile_image_url = extra_data['profile_image_url']
            user.date_joined = extra_data['created_at']
            user.save()
