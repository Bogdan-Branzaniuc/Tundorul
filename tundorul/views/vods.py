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
        vods = []
        vods_data = Vods.objects.filter()

        for vod_data in vods_data:

            vod = {
                'title': vod_data.title,
                'published_at': vod_data.published_at,
                'url': vod_data.url,
                'thumbnail_url': vod_data.thumbnail_url,
                'view_count': vod_data.view_count,
                'stream_id': vod_data.stream_id,
            }
            if vod not in vods:
                vods.append(vod)
            print(vod_data.title)

        context = {
            'vods': vods
        }

        return render(
            request,
            'vods.html',
            context,
        )