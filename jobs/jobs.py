from django.conf import settings
import requests
import os


def twitch_schedule():
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