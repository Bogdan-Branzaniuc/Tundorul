from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import twitch_app_token, twitch_schedule_callendar, twitch_get_vods
import os

def start():
    scheduler = BackgroundScheduler()

    scheduler.add_job(twitch_app_token, 'interval', seconds=4704769)
    scheduler.add_job(twitch_schedule_callendar, 'interval', hours=6)
    scheduler.add_job(twitch_get_vods, 'interval', hours=6)
    scheduler.start()
