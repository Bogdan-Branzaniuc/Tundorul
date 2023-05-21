from django_unicorn.components import UnicornView
from django.contrib import messages
from django.shortcuts import get_object_or_404
from tundorul.models import Suggestions, UserProfile
from django.db import IntegrityError

class SuggestionsView(UnicornView):
    name = "suggestions_comp_view"

    suggestions = None
    voted_suggestions = None


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = kwargs.get("name")
        self.submit_suggestion_content = ''
        self.submit_suggestion_title = ''
        self.upvote_suggestion_title = ''

    def mount(self, *args, **kwargs):
        self.user_profile = UserProfile.objects.get(current_name=self.request.user.username)
        self.suggestions = Suggestions.objects.filter(approved=True)
        self.unaproved_suggestions = Suggestions.objects.filter(approved=False)
        self.voted_suggestions = list(self.suggestions.filter(upvotes=self.user_profile).values_list('title', flat=True))
        return super().mount()

    def submit_suggestion(self):
        title = self.submit_suggestion_title
        body = self.submit_suggestion_content
        author = self.user_profile
        print(self.submit_suggestion_title)
        print(self.submit_suggestion_content)
        try:
            suggestion = Suggestions.objects.create(
                title=title,
                body=body,
                author=author,
            )
            suggestion.save()
            messages.success(self.request, 'Your suggestion is awaiting approval.')
        except IntegrityError:
            messages.error(self.request, "There is one suggestion with this title Already, you can change the title or upvote the current one if it's content is the same")
            pass

        self.suggestions = Suggestions.objects.filter(approved=True)
        self.unaproved_suggestions = Suggestions.objects.filter(approved=False)
        self.voted_suggestions = list(self.suggestions.filter(upvotes=self.user_profile).values_list('title', flat=True))


    def submit_upvote(self, id):
        suggestion = suggestion = get_object_or_404(Suggestions, id=id)
        if suggestion.upvotes.filter(id=self.user_profile.id).exists():
            suggestion.upvotes.remove(self.user_profile)
            suggestion.votes -= 1
            suggestion.save()
        else:
            suggestion.upvotes.add(self.user_profile)
            suggestion.votes += 1
            suggestion.save()
        self.suggestions = Suggestions.objects.filter(approved=True)
        self.voted_suggestions = list(self.suggestions.filter(upvotes=self.user_profile).values_list('title', flat=True))