from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class UserProfile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_related')
    uid = models.CharField(max_length=200, default='')
    current_name = models.CharField(max_length=200, default='')
    email = models.EmailField(max_length=200, default='')
    channel_points = models.IntegerField(default=0)
    is_subscribed = models.BooleanField()

    class Meta:
        ordering = ['-username']

    def __str__(self):
        return self.current_name


#class Game(models.Model):


#class Giveaway(models.Model):
