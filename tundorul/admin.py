from django.contrib import admin
from .models import UserProfile, Vods, Suggestions

admin.site.register(UserProfile)
admin.site.register(Vods)
admin.site.register(Suggestions)

