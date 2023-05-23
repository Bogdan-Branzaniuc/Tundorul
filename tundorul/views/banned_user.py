from django.views.generic import TemplateView

class BannedUser(TemplateView):
    template_name = 'banned_user.html'