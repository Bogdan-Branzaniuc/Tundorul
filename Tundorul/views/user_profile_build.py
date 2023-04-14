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
    # else:
    #     print("SOCIAL ACCOUNT missing!!!!!!!!!!!!!!")
    #     print("SOCIAL ACCOUNT ADDED!!!!!!!!!!!!!!")
    #     print(social_usser.__dir__)
    #     print(social_usser.extra_data)
    #     user_profile = UserProfile.objects.create(
    #         username=social_usser.user,
    #         uid=social_usser.extra_data['id'],
    #         current_name=social_usser.extra_data['display_name'],
    #         email=user.email,
    #         join_date=datetime.strptime('2000/10/06', '%Y/%m/%d'),
    #         time_watched=datetime(2000, 10, 20),
    #         channel_points=150,
    #         is_subscribed=True,
    #         subscribed_since=datetime(2000, 10, 20),
    #     )
    #     user_profile.save()


# @receiver(social_account_signed_up)
# def user_signed_up(sender, request, user, **kwargs):
#     print('signedUp')