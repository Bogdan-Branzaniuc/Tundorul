from django import forms


class CreateSuggestionForm(forms.Form):
    suggestion_title = forms.CharField(min_length=3, max_length=50, required=True)
    suggestion_content = forms.CharField(min_length=10, max_length=500, required=True)


class EditSuggestionForm(forms.Form):
    edit_suggestion_title = forms.CharField(min_length=3, max_length=50, required=True)
    edit_suggestion_content = forms.CharField(min_length=10, max_length=500, required=True)