from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from Tundorul.models import StreamSchedule
from allauth.socialaccount.models import SocialToken, SocialAccount
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
import requests
import os
import json


@receiver(post_save, sender=StreamSchedule)
def saveSegmentsOnTwitch(sender, instance, **kwargs):
    query_set_user = SocialAccount.objects.filter(uid=os.environ.get('ADMIN_USER_ID'))
    social_user = get_object_or_404(query_set_user)
    query_set_token = SocialToken.objects.filter(account=social_user)
    social_user_admin_token = get_object_or_404(query_set_token).token


    query_set = StreamSchedule.objects.all()
    for segment_instance in query_set:
        instance_dict = {field.name: getattr(segment_instance, field.name) for field in segment_instance._meta.fields}
        start_time = instance_dict['start_time'].strftime('%Y-%m-%dT%H:%M:%SZ')
        if instance_dict['soft_deleted'] and instance_dict['segment_id']:
            #all records with softdeleted flag set to true will send a DELETE request
            # broadcaster_id : socialuser.uid
            # id: segment_id
            pass
        elif instance_dict['segment_id']:
            # all records with an id and field deleted=false will send a Patch request

            # start_time
            # duration
            # category_id
            # is_canceled
            # timezone
            pass
        else:
            # all records without an ID will send a Post request , and then get their id's saved
            # to be tested with real affiliate account.
            headers = {
                'Authorization': 'Bearer ' + social_user_admin_token,
                'Client-Id': os.environ.get('CLIENT_ID'),
                'Content-Type': 'application/json',
            }
            params = {
                'broadcaster_id': os.environ.get('ADMIN_USER_ID'),
            }
            json_data = {
                "start_time": start_time,
                "timezone": instance_dict['timezone'],
                "duration": str(instance_dict['duration']),
                "is_recurring": instance_dict['is_recurring'],
                "title": instance_dict['title'],
            }
            json_object = json.dumps(json_data)
            url = 'https://api.twitch.tv/helix/schedule/segment'
            result = requests.post(url, params=params, headers=headers, json=json_object)
            print(result)

    "at the end delete any soft_deleted True fields."

    print('this was runned', instance.start_time)





