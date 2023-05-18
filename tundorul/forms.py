from django import forms

class SuggestionForm(forms.Form):
    title = forms.CharField(max_length=100)
    body = forms.CharField(widget=forms.Textarea)

class UpvoteForm(forms.Form):
    # Add any fields you need for the upvote form
    pass