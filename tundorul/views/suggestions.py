from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
import requests
from tundorul.models import Suggestions, UserProfile
from django.db import IntegrityError

class SuggestionsView(View):

    def get(self, request, *args, **kwargs):
        suggestions = Suggestions.objects.all()
        context = {
            'suggestions': suggestions,
        }
        return render(
            request,
            'suggestions.html',
            context,
        )

    def post(self, request, *args, **kwargs):
        print(request.POST.get('title'))
        print(request.POST.get('body'))
        print(request.user)
        title = request.POST.get('title')
        body = request.POST.get('body')
        user_profile = UserProfile.objects.get(current_name=request.user.username)
        

        try:
            suggestion = Suggestions.objects.create(
                title=title,
                body=body,
                author=request.user.username,
                user_profile=user_profile,
            )
            suggestion.save()
            messages.success(request, 'Your suggestion is awaiting approval.')
        except IntegrityError:
            messages.error(request, "There is one suggestion with this title Already, you can change the title or upvote the current one if it's content is the same")
            pass

        suggestions = Suggestions.objects.all()
        context = {
            'suggestions': suggestions,
        }
        return render(
            request,
            'suggestions.html',
            context,
        )