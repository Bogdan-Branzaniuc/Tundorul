from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from Tundorul.models import StreamSchedule
from django.http import HttpResponseRedirect
from django.contrib import messages
import requests

class Home(View):

    def get(self, request, *args, **kwargs):
        schedule_array = []
        query_set = StreamSchedule.objects.all()

        for instance in query_set:
            instance_dict = [getattr(instance, field.name) for field in instance._meta.fields]
            schedule_array.append(instance_dict)

        print(schedule_array)
        context = {
            'schedule': schedule_array
        }
        StreamSchedule
        return render(
            request,
            'index.html',
            context,

        )
