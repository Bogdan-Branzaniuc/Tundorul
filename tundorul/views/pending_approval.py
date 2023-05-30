from django.shortcuts import render
from django.views import View
from suggestion.models import Suggestions


class PendingApproval(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_staff:
            suggestions = Suggestions.objects.filter(approved=False)
            context = {
                'suggestions': suggestions,
            }
            return render(
                request,
                'pending_approval.html',
                context,
            )
        else:
            return render(
                request,
                'index.html',
            )

    def post(self, request, *args, **kwargs):
        titles = request.POST.getlist('title')
        for title in titles:
            approved = request.POST.get(title)
            if approved == 'on':
                suggestion = Suggestions.objects.get(title=title)
                suggestion.approved = True
                suggestion.save()
        suggestions = Suggestions.objects.filter(approved=False)
        context = {
            'suggestions': suggestions,
        }

        return render(
            request,
            'pending_approval.html',
            context,
        )