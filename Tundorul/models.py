from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "draft"), (1, "Published"))


class UserProfile(models.Model):
    username = models.ForeignKey(
        User, on_delete = models.CASCADE, related_name='user_profile'
    )
    user_token = models.CharField(max_length=200)
    email = models.EmailField()
    join_date = models.DateField()
    time_watched = models.TimeField()
    channel_points = models.IntegerField()
    is_subscribed = models.BooleanField()
    subscribed_since = models.TimeField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-join_date']

    def __str__(self):
        return self.username