from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from Tundorul.models import StreamSchedule
from allauth.socialaccount.models import SocialToken, SocialAccount
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
import requests
from django.http import HttpResponse
from django.templatetags.static import static
import os


# def twitch_calendar(request):
#
#     response = requests.get('https://api.twitch.tv/helix/schedule/icalendar?broadcaster_id=453874993')
#     print(response.content)
#     file_path = os.path.join('static', 'twitchdev.ics')
#     with open(file_path, 'wb') as file:
#         file.write(response.content)
#     file_url = request.build_absolute_uri(static(file_path))
#     html = f'<iframe src="{file_url}" style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>'
#     "at the end delete any soft_deleted True fields."
#     return HttpResponse(html)
#     print('this was runned', instance.start_time)





