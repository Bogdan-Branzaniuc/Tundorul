from django_unicorn.components import UnicornView
from django.contrib import messages
from django.shortcuts import get_object_or_404
from tundorul.models import Suggestions, UserProfile
from django.db import IntegrityError
from suggestion.forms import CreateSuggestionForm, EditSuggestionForm


class SuggestionsView(UnicornView):
    suggestions = None
    voted_suggestions = None
    unaproved_suggestions = None
    user_profile = None
    personal_suggestions = None

    form_class = CreateSuggestionForm
    suggestion_title = ''
    suggestion_content = ''
    edit_suggestion_title = ''
    edit_suggestion_content = ''

    filter_by_votes = False
    filter_ownership_mine = False
    filter_unapproved = False
    confirm_delete_popup = None
    confirm_edit_popup = None

    def mount(self, *args, **kwargs):
        self.user_profile = UserProfile.objects.get(current_name=self.request.user.username)
        self.suggestions = Suggestions.objects.filter(approved=True)
        self.voted_suggestions = list(self.suggestions.filter(upvotes=self.user_profile).values_list('title', flat=True))
        self.personal_suggestions = Suggestions.objects.filter(author=self.user_profile)
        self.filter_by_votes = False
        self.filter_ownership_mine = False
        self.filter_unapproved = False
        self.confirm_delete_popup = -1
        self.confirm_edit_popup = -1
        self.form_class = CreateSuggestionForm
        return super().mount()

    def submit_suggestion(self):
        author = self.user_profile
        if self.is_valid():
            try:
                suggestion = Suggestions.objects.create(
                    title=self.suggestion_title,
                    body=self.suggestion_content,
                    author=author,
                )
                suggestion.save()
                messages.success(self.request, 'Your suggestion is awaiting approval.')
            except IntegrityError:
                messages.error(self.request, "There is one suggestion with this title Already, you can change the title or upvote the current one if it's content is the same")
                pass
        self.filter_suggestions()

    def submit_upvote(self, suggestion_id):
        suggestion = get_object_or_404(Suggestions, id=suggestion_id)
        if suggestion.upvotes.filter(id=self.user_profile.id).exists():
            suggestion.upvotes.remove(self.user_profile)
            suggestion.votes -= 1
            suggestion.save()
        else:
            suggestion.upvotes.add(self.user_profile)
            suggestion.votes += 1
            suggestion.save()
        self.filter_suggestions()

    def edit_suggestion(self, suggestion_id):
        self.confirm_edit_popup = suggestion_id
        self.form_class = EditSuggestionForm
        self.filter_suggestions()

    def submit_edit_suggestion(self, suggestion_id, cancel):
        if cancel:
            pass
        else:
            if self.is_valid():
                try:
                    suggestion = get_object_or_404(Suggestions, id=suggestion_id)
                    suggestion.title = self.suggestion_title
                    suggestion.body = self.suggestion_content
                    suggestion.approved = False
                    suggestion.save()
                    messages.success(self.request, 'Your edit is awaiting approval.')
                except IntegrityError:
                    messages.error(self.request, "Sorry!, There is one suggestion with this title Already")
                    pass
        self.confirm_edit_popup = -1
        self.form_class = CreateSuggestionForm
        self.filter_suggestions()

    def delete_suggestion(self, suggestion_id, cancel):
        if cancel:
            pass
        else:
            suggestion = Suggestions.objects.filter(id=suggestion_id)
            suggestion.delete()
            self.filter_suggestions()
        self.confirm_delete_popup = -1
        self.filter_suggestions()

    def show_confirm_deletion(self, suggestion_id):
        self.confirm_delete_popup = suggestion_id
        self.filter_suggestions()

    def filter_suggestions(self):
        if self.filter_ownership_mine is False and self.filter_unapproved is False:
            self.suggestions = Suggestions.objects.filter(approved=True)
        elif self.filter_ownership_mine is True and self.filter_unapproved is False:
            self.suggestions = Suggestions.objects.filter(author=self.user_profile, approved=True)
        else:
            self.suggestions = Suggestions.objects.filter(author=self.user_profile, approved=False)
        # order by votes or date
        if self.filter_by_votes is True:
            self.suggestions = self.suggestions.order_by('-votes')
        else:
            self.suggestions = self.suggestions.order_by('-published_at')
        self.voted_suggestions = list(self.suggestions.filter(upvotes=self.user_profile).values_list('title', flat=True))
        self.personal_suggestions = Suggestions.objects.filter(author=self.user_profile)

    def awaiting_approval(self):
        self.filter_unapproved = False if self.filter_unapproved is True else True
        if self.filter_unapproved is True:
            self.filter_ownership_mine = True
        self.filter_suggestions()

    def show_mine(self):
        self.filter_ownership_mine = False if self.filter_ownership_mine is True else True
        self.filter_suggestions()

    def by_votes(self):
        self.filter_by_votes = False if self.filter_by_votes is True else True
        self.filter_suggestions()