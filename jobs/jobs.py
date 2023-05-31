from tundorul.models import Vods
from django.db import IntegrityError
import requests
import os
import json


def twitch_app_token():
    """
    Will make a request to retrieve an app access token from twitch
    """
    app_token_url = 'https://id.twitch.tv/oauth2/token'
    params = {
        'client_id': os.environ.get('CLIENT_ID'),
        'client_secret': os.environ.get('CLIENT_SECRET'),
        'grant_type': 'client_credentials',
    }
    app_access_token = requests.post(app_token_url, params=params)
    try:
        if app_access_token.status_code == 200:
            token = json.loads(app_access_token.content.decode("utf-8"))
            os.environ["APP_TOKEN"] = token['access_token']
        else:
            app_access_token.raise_for_status()
    except requests.exceptions.HTTPError as e:
        pass


def twitch_schedule_callendar():
    """
    Updates the static file twitchdev.ics, that renders the streammer's schedule in the home.py view
    """
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
        pass
        # following updates


def twitch_get_vods():
    """
    retrieves the last 10 vods from twitch and updates the Vods model
    """
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
    if vods.status_code == 200:
        Vods.objects.all().delete()
        data = vods.json()
        for field in data['data']:
            vod = Vods.objects.create(
                id=field['id'],
                title=field['title'],
                url=field['url'],
                thumbnail_url=field['thumbnail_url'],
                published_at=field['published_at'],
                view_count=field['view_count'],
                stream_id=field['id'],
            )
            try:
                vod.save()
            except IntegrityError:
                continue
