from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import twitch_schedule

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(twitch_schedule, 'interval', hours=6)
    scheduler.start()
