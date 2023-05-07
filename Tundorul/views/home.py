from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect, HttpResponse
import requests
import pandas as pd
import datetime
from icalendar import Calendar
import icalendar
from icalevents.icalevents import events
import os
from TundorulDjango import settings
from collections import Counter


class Home(View):
    def get(self, request, *args, **kwargs):
        file_path = os.path.join(settings.STATICFILES_DIRS[0], 'twitchdev.ics')
        calendar_file = open(file_path)
        calendar = Calendar.from_ical(calendar_file.read())
        general_start_hour = []
        twitch_events = []

        for component in calendar.walk():
            if component.name == 'VEVENT':
                print(component)
                component_object = {}
                dtstart_prop = component.get('DTSTART')
                dtstart_date = dtstart_prop.dt.strftime('%Y-%m-%d')
                dtstart_time = dtstart_prop.dt.strftime('%H:%M')

                weekday = dtstart_prop.dt.strftime('%A')

                event_summary = component['SUMMARY']
                event_title = component['DESCRIPTION']
                component_object['title'] = event_title.replace('.', ' ')
                component_object['start_date'] = dtstart_date
                component_object['start_time'] = dtstart_time
                component_object['summary'] = event_summary
                component_object['day'] = weekday
                component_object['weekday_integer'] = dtstart_prop.dt.weekday() + 1 % 7 #makes the week start on Sunday instead of monday, needed for JS compatibility in the template

                general_start_hour.append(dtstart_time)
                twitch_events.append(component_object)
        calendar_file.close()
        sorted_events = sorted(twitch_events, key=lambda o: o['weekday_integer'])
        schedule_heading = {
            'days_per_week': len(sorted_events),
            'from_hour': Counter(general_start_hour).most_common(1)[0][0],
        }

        context = {
            'events': sorted_events,
            'heading': schedule_heading,
        }

        return render(
            request,
            'index.html',
            context,
        )
