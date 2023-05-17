from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
import requests
from tundorul.models import Suggestions, UserProfile

class PendingApproval(View):
    def get(self, request, *args, **kwargs):
        suggestions = Suggestions.objects.all()
        context = {
            'suggestions': suggestions,
        }
        return render(
            request,
            'pending_approval.html',
            context,
        )

    def post(self, request, *args, **kwargs):
        print(request.POST)
        suggestions = Suggestions.objects.all()
        context = {
            'suggestions': suggestions,
        }

        return render(
            request,
            'pending_approval.html',
            context,
        )