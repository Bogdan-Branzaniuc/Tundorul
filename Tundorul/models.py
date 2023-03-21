from django.db import models
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import AbstractUser
from django.db import migrations, models
import django.contrib.auth.models

STATUS = ((0, "draft"), (1, "Published"))

class userSocial(AbstractUser):
    USERNAME_FIELD = 'uid'
    uid = models.CharField(max_length=200, unique=True)
    last_login = models.DateField()
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.EmailField()
    date_joined = models.DateField(auto_now_add=True)
    profile_image_url = models.URLField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-date_joined']

    def __str__(self):
        return self.username

