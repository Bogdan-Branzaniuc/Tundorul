from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
import requests
from tundorul.models import Suggestions, UserProfile
from django.db import IntegrityError
from ..forms import SuggestionForm, UpvoteForm
from django.http import HttpResponse



class SuggestionsView(View):
    def get(self, request, *args, **kwargs):
        user_profile = UserProfile.objects.get(current_name=request.user.username)
        suggestions = Suggestions.objects.filter(approved=True)
        suggestion_form = SuggestionForm()
        upvote_form = UpvoteForm()
        voted_suggestions = suggestions.filter(upvotes=user_profile).values_list('title', flat=True)
        context = {
            'suggestion_form': suggestion_form,
            'upvote_form': upvote_form,
            'suggestions': suggestions,
            'voted_suggestions': voted_suggestions,
        }
        return render(
            request,
            'suggestions.html',
            context,
        )

    def post(self, request, *args, **kwargs):
        user_profile = UserProfile.objects.get(current_name=request.user.username)
        print(request.POST)
        if 'submit_suggestion' in request.POST:

            suggestion_form = SuggestionForm(request.POST)
            if suggestion_form.is_valid():
                print(request.POST)
                print(request.POST.get('title'))
                print(request.POST.get('body'))
                print(request.user)
                title = request.POST.get('title').strip()
                body = request.POST.get('body').strip()
                author = UserProfile.objects.get(current_name=request.user.username)

                try:
                    suggestion = Suggestions.objects.create(
                        title=title,
                        body=body,
                        author=author,
                    )
                    suggestion.save()
                    messages.success(request, 'Your suggestion is awaiting approval.')
                except IntegrityError:
                    messages.error(request, "There is one suggestion with this title Already, you can change the title or upvote the current one if it's content is the same")
                    pass

        elif 'submit_upvote' in request.POST:
            upvote_form = UpvoteForm(request.POST)
            print(123)
            print(request.POST)
            if upvote_form.is_valid():
                title = request.POST['submit_upvote']
                suggestion = get_object_or_404(Suggestions, title=title)
                if suggestion.upvotes.filter(id=user_profile.id).exists():
                    suggestion.upvotes.remove(user_profile)
                    suggestion.votes -= 1
                    suggestion.save()
                else:
                    suggestion.upvotes.add(user_profile)
                    suggestion.votes += 1
                    suggestion.save()

        suggestions = Suggestions.objects.filter(approved=True)
        suggestion_form = SuggestionForm()
        upvote_form = UpvoteForm()
        voted_suggestions = suggestions.filter(upvotes=user_profile).values_list('title', flat=True)

        response = {'message': '11233'}
        return render(
            request,
            'suggestions.html',
        )