from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from Tundorul.models import StreamSchedule
from django.contrib.staticfiles.storage import staticfiles_storage
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
import requests
import pandas as pd
import datetime
from icalendar import Calendar
import icalendar
from icalevents.icalevents import events
import os
from TundorulDjango import settings

class Home(View):
    def get(self, request, *args, **kwargs):

        file_path = os.path.join(settings.STATICFILES_DIRS[0], 'twitchdev.ics')
        calendar_file = open(file_path)
        calendar = Calendar.from_ical(calendar_file.read())
        events = []
        for component in calendar.walk():
            if component.name == 'VEVENT':
                print(component)
                component_object = {}
                dtstart_prop = component.get('DTSTART')
                dtstart_date = dtstart_prop.dt.strftime('%Y-%m-%d')
                dtstart_time = dtstart_prop.dt.strftime('%H:%M')

                event_summary = component['SUMMARY']
                event_title = component['DESCRIPTION']
                component_object['title'] = event_title
                component_object['start_date'] = dtstart_date
                component_object['start_time'] = dtstart_time
                component_object['summary'] = event_summary
                events.append(component_object)
        calendar_file.close()
        context = {
            'events': events,
        }

        return render(
            request,
            'index.html',
            context,
        )
