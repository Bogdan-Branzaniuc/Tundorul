from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from Tundorul.models import StreamSchedule
from django.http import HttpResponseRedirect
from django.contrib import messages
import requests
import pandas as pd
import datetime

class Home(View):

    def get(self, request, *args, **kwargs):
        admin_vacation = False #retrieve this from admin user profile instance.
        schedule_array = []
        query_set = StreamSchedule.objects.all()
        for instance in query_set:
            start_date = instance.start_time.strftime('%Y-%m-%d')
            start_hour = instance.start_time.strftime('%H:%M')
            instance_dict = {field.name: getattr(instance, field.name) for field in instance._meta.fields}
            instance_dict['start_hour'] = start_hour
            instance_dict['start_date'] = start_date
            dateObject = datetime.datetime.strptime(instance_dict['start_date'], '%Y-%m-%d')
            instance_dict['day'] = dateObject.strftime('%A')
            schedule_array.append(instance_dict)
        # change this list for convenience.
        dates = pd.date_range(datetime.datetime.today().strftime('%Y-%m-%d'), periods=20).tolist()
        formnatted_dates = [{'date': d.date().strftime('%Y-%m-%d'), 'day':d.date().strftime('%A')} for d in dates]

        context = {
            'schedule': schedule_array,
            'showing_dates': formnatted_dates,
            'admin_vacation': admin_vacation,
        }
        StreamSchedule
        return render(
            request,
            'index.html',
            context,

        )
