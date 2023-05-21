from django.shortcuts import render
from django.views.generic import TemplateView

class SuggestionsView(TemplateView):
    template_name = "suggestions.html"
