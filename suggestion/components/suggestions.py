from django_unicorn.components import UnicornView
from django.contrib import messages
from django.shortcuts import get_object_or_404
from tundorul.models import Suggestions, UserProfile
from django.db import IntegrityError
from suggestion.forms import CreateSuggestionForm


class SuggestionsView(UnicornView):
    suggestions = None
    voted_suggestions = None
    unaproved_suggestions = None
    user_profile = None
    personal_suggestions = None

    form_class = CreateSuggestionForm
    title = ''
    content = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filter = None

    def mount(self, *args, **kwargs):
        self.user_profile = UserProfile.objects.get(current_name=self.request.user.username)
        self.suggestions = Suggestions.objects.filter(approved=True)
        self.unaproved_suggestions = Suggestions.objects.filter(approved=False)
        self.voted_suggestions = list(self.suggestions.filter(upvotes=self.user_profile).values_list('title', flat=True))
        self.personal_suggestions = Suggestions.objects.filter(author=self.user_profile)

        return super().mount()

    def submit_suggestion(self):
        author = self.user_profile
        if self.is_valid():
            try:
                suggestion = Suggestions.objects.create(
                    title=self.title,
                    body=self.content,
                    author=author,
                )
                suggestion.save()
                messages.success(self.request, 'Your suggestion is awaiting approval.')
            except IntegrityError:
                messages.error(self.request, "There is one suggestion with this title Already, you can change the title or upvote the current one if it's content is the same")
                pass

        self.suggestions = self.filter()
        self.voted_suggestions = list(self.suggestions.filter(upvotes=self.user_profile).values_list('title', flat=True))
        self.personal_suggestions = Suggestions.objects.filter(author=self.user_profile)

    def submit_upvote(self, id):
        suggestion = get_object_or_404(Suggestions, id=id)
        if suggestion.upvotes.filter(id=self.user_profile.id).exists():
            suggestion.upvotes.remove(self.user_profile)
            suggestion.votes -= 1
            suggestion.save()
        else:
            suggestion.upvotes.add(self.user_profile)
            suggestion.votes += 1
            suggestion.save()
        self.suggestions = self.filter()

    def approve(self, id):
        pass

    def disapprove(self, id):
        pass

    def edit_suggestion(self, id):
        suggestion = get_object_or_404(Suggestions, id=id)

    def delete_suggestion(self, id):
        suggestion = Suggestions.objects.filter(id=id)
        print(suggestion)

        suggestion.delete()
        self.suggestions = Suggestions.objects.filter(approved=True)
        self.voted_suggestions = list(
        self.suggestions.filter(upvotes=self.user_profile).values_list('title', flat=True))
        self.personal_suggestions = Suggestions.objects.filter(author=self.user_profile)

    def awaiting_approval(self):
        self.filter = self.awaiting_approval
        self.suggestions = Suggestions.objects.filter(approved=False)
        return self.suggestions

    def show_mine(self):
        self.filter = self.show_mine
        self.suggestions = Suggestions.objects.filter(author=self.user_profile)
        return self.suggestions

    def show_all(self):
        self.filter = self.show_all
        self.suggestions = Suggestions.objects.all()
        return self.suggestions

    def by_date(self):
        self.filter = self.by_date
        self.suggestions = Suggestions.objects.all().order_by('-published_at')

    def by_votes(self):
        self.filter = self.by_votes
        self.suggestions = Suggestions.objects.all().order_by('-votes')
        return self.suggestions