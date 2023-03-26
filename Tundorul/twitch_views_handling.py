from twitchAPI.twitch import Twitch, AuthScope
import twitchAPI
from twitchAPI.helper import first
import asyncio
import requests
from django.views import generic, View


async def twitch_example():
    twitch = await Twitch('hf3ftyp7rubp7kdu4ebr7fy0flzba8', 'boxcbhf9h2yhd1vqhh39xiqh7xs69c')

    # print the ID of your user or do whatever else you want with it
    broadcaster = await first(twitch.get_users(logins='notonuclearwar'))
    user = await first(twitch.get_users(logins='lalapetala'))
    print(user.id)
   #test_user username = lalapetala
   #test user password = petalalalapedala
    #code = '8bcb9bdtjxk3prkaw8lntub22qs8br'
    code ='secknl31yneo5wpgvv9mufz9vz5yqz'
    headers = {
        'Client-ID': 'hf3ftyp7rubp7kdu4ebr7fy0flzba8',
        'Authorization': code
    }

    broadcaster_id = broadcaster.id
    user_id = user.id

    url = f'https://api.twitch.tv/helix/subscriptions/user?broadcaster_id={broadcaster_id}&user_id={user_id}'

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()['data']
        if data:
            # User is a subscriber to the channel
            print(f'{user_id} is a subscriber to {broadcaster_id}')
        else:
            # User is not a subscriber to the channel
            print(f'{user_id} is not a subscriber to {broadcaster_id}')
    else:
        print('Error:', response.status_code)

# run this example
asyncio.run(twitch_example())



