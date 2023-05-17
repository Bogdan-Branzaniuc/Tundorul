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
    profile_picture_url = models.TextField(blank=True)

    class Meta:
        ordering = ['-username']

    def __str__(self):

        return self.current_name


class Vods(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField(blank=True)
    url = models.CharField(max_length=255)
    thumbnail_url = models.TextField(blank=True)
    published_at = models.DateTimeField()
    view_count = models.IntegerField(default=0)
    stream_id = models.CharField(max_length=255, default=0, unique=True)

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Suggestions(models.Model):
    title = models.TextField(unique=True)
    body = models.TextField(blank=True)
    author = models.TextField()
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        related_name='suggestion'
    )
    published_at = models.DateTimeField(auto_now_add=True)
    votes = models.IntegerField(default=0)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.title