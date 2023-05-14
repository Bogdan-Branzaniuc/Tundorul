from django.conf import settings
from allauth.socialaccount.models import SocialToken, SocialAccount
from django.shortcuts import get_object_or_404
import requests
import os
import json
import time

def twitch_app_token():
    app_token_url = ' https://id.twitch.tv/oauth2/token'
    params = {
        'client_id': os.environ.get('CLIENT_ID'),
        'client_secret': os.environ.get('CLIENT_SECRET'),
        'grant_type': 'client_credentials',
    }
    app_access_token = requests.post(app_token_url, params=params)
    attempt = 0
    try:
        if app_access_token.status_code == 200:
            token = json.loads(app_access_token.content.decode("utf-8"))
            os.environ["APP_TOKEN"] = token['access_token']
            return token['expires_in']
            attempt += 1
        else:
            if attempt > 3:
                app_access_token.raise_for_status()
            else:
                time.sleep(attempt)
                return twitch_app_token()
    except requests.exceptions.HTTPError as e:
        print(f"Failed to retrieve app_token: {e}")


def twitch_schedule_callendar():
    url = 'https://api.twitch.tv/helix/schedule/icalendar?'
    data ={
        'broadcaster_id': os.environ.get('ADMIN_USER_ID'),
    }
    response = requests.get(url, params=data)
    try:
        if response.status_code == 200:
            file_path = os.path.join('static', 'twitchdev.ics')
            with open(file_path, 'wb') as file:
                file.write(response.content)
                file.close()
        else:
            response.raise_for_status()  # raise HTTPError exception if status code is not 200
    except requests.exceptions.HTTPError as e:
        print(f"Failed to download schedule: {e}")


def twitch_get_vods():
    app_access_token = os.environ.get("APP_TOKEN")
    headers = {
        'Authorization': 'Bearer ' + app_access_token,
        'Client-Id': os.environ.get('CLIENT_ID'),
    }
    params = {
        'user_id': os.environ.get('ADMIN_USER_ID'),
        'first': '10',
    }
    url = 'https://api.twitch.tv/helix/videos'

    vods = requests.get(url, headers=headers, params=params)
    attempt = 0
    try:
        if vods.status_code == 200:
            data = vods.json()
            for field in data['data']:
                print(field)
        else:
            if attempt > 3:
                vods.raise_for_status()
            else:
                attempt += 1
                return twitch_get_vods()

    except requests.exceptions.HTTPError as e:
        print(f"Failed to retrieve Vods {e}")
