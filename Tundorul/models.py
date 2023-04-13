from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField

from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class UserProfile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_related')
    uid = models.CharField(max_length=200, default='0000000')
    current_name = models.CharField(max_length=200, default='0000000')
    email = models.EmailField()
    following_since = models.DateField()
    time_watched = models.TimeField()
    channel_points = models.IntegerField()
    is_subscribed = models.BooleanField()
    subscribed_since = models.TimeField()

    class Meta:
        ordering = ['-username']

    def __str__(self):
        return self.current_name

