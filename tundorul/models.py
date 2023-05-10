from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from datetime import datetime


class UserProfile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_related')
    uid = models.CharField(max_length=200, default='')
    current_name = models.CharField(max_length=200, default='')
    email = models.EmailField(max_length=200, default='')

    is_subscribed = models.BooleanField(default=False)
    is_follower = models.BooleanField(default=False)
    is_banned = models.BooleanField(default=False)
    join_date = models.DateField(auto_now_add=True, blank=True)

    class Meta:
        ordering = ['-username']

    def __str__(self):
        return self.current_name


#class Game(models.Model):
    #crono_id =
    #title =
    #period =
    #description =
    #events =

    # class Meta:
    #     ordering = ['-start_time']
    #
    # def __str__(self):
    #     return self.title

#class Vods.