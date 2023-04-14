from django.contrib import admin
from .models import UserProfile
from .models import StreamSchedule

admin.site.register(UserProfile)
admin.site.register(StreamSchedule)

