from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
import requests
from tundorul.models import UserProfile
from suggestion.models import Suggestions


class PendingApproval(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_staff:
            suggestions = Suggestions.objects.filter(approved=False)
            context = {
                'suggestions': suggestions,
            }
            return render(
                request,
                'pending_approval.html',
                context,
            )
        else:
            return render(
                request,
                'index.html',
            )

    def post(self, request, *args, **kwargs):
        titles = request.POST.getlist('title')
        print(request.POST)
        print(titles)
        for title in titles:
            print(title)
            approved = request.POST.get(title)
            if approved == 'on':
                suggestion = Suggestions.objects.get(title=title)
                suggestion.approved = True
                suggestion.save()
        suggestions = Suggestions.objects.filter(approved=False)
        context = {
            'suggestions': suggestions,
        }

        return render(
            request,
            'pending_approval.html',
            context,
        )