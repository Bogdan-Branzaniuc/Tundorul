from Tundorul.models import UserProfile
from allauth.socialaccount.models import SocialAccount
from datetime import datetime

from allauth.socialaccount.signals import pre_social_login
from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from allauth.socialaccount.models import SocialAccount, SocialToken
import requests


@receiver(pre_social_login)
def update_or_create_user_profile(request, sociallogin, **kwargs):
    print(sociallogin.token)

    if UserProfile.objects.filter(username=sociallogin.user).exists():
        pass
    else:
        print(sociallogin.__dir__())

        extra_data = sociallogin.account.extra_data
        token = sociallogin.token

        user_profile = UserProfile.objects.create(
         username=sociallogin.user,
         uid=extra_data['id'],
         current_name=extra_data['display_name'],
         email=extra_data['email'],
         # channel_points=150,
         is_subscribed=True,
         # subscribed_since=datetime(2000, 10, 20),
        )
        user_profile.save()


# @receiver(social_account_signed_up)
# def user_signed_up(sender, request, user, **kwargs):
#     print('signedUp')