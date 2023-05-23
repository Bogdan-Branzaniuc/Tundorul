from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404, reverse, redirect
from tundorul.models import UserProfile

class SuggestionsView(TemplateView):
    template_name = "suggestions.html"

    def get(self, request, *args, **kwargs):
        if (request.user.is_authenticated):
            user_profile = get_object_or_404(UserProfile, username=request.user)
            if user_profile.is_banned is True:
                return redirect('banned_user')