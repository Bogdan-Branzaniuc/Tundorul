from django import forms


class CreateSuggestionForm(forms.Form):
    title = forms.CharField(min_length=3, max_length=50, required=True)
    content = forms.CharField(min_length=10, max_length=500, required=True)