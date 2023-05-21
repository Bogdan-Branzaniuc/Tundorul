from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.contrib import messages
from tundorul.models import Suggestions, UserProfile




class SuggestionsView(View):
    def get(self, request, *args, **kwargs):
        user_profile = UserProfile.objects.get(current_name=request.user.username)
        suggestions = Suggestions.objects.filter(approved=True)
        voted_suggestions = suggestions.filter(upvotes=user_profile).values_list('title', flat=True)
        context = {
            'suggestions': suggestions,
            'voted_suggestions': voted_suggestions,
        }
        return render(
            request,
            'suggestions.html',
            context,
        )