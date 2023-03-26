from .models import UserProfile
from allauth.socialaccount.models import SocialAccount
from datetime import datetime
from allauth.socialaccount.signals import social_account_updated
from allauth.account.signals import user_signed_up
from django.dispatch import receiver
import sys
sys.path.insert(1, '/workspace/tundorul/project_venv/lib/python3.8/site-packages/twitchAPI/')
from twitchAPI import Twitch

@receiver(user_signed_up)
def user_signed_up(sender, request, user, **kwargs):
    print('account signed up')
    print(user.__dir__())
    social_usser = SocialAccount.objects.get(user=user)

    if UserProfile.objects.filter(username=user).exists():
        print("record here")
    else:
        print("SOCIAL ACCOUNT missing!!!!!!!!!!!!!!")
        print("SOCIAL ACCOUNT ADDED!!!!!!!!!!!!!!")
        print(social_usser.__dir__)
        print(social_usser.extra_data)
        user_profile = UserProfile.objects.create(
            username=social_usser.user,
            uid=social_usser.extra_data['id'],
            current_name=social_usser.extra_data['display_name'],
            email=user.email,
            join_date=datetime.strptime('2000/10/06', '%Y/%m/%d'),
            time_watched=datetime(2000, 10, 20),
            channel_points=150,
            is_subscribed=True,
            subscribed_since=datetime(2000, 10, 20),
        )
        user_profile.save()

@receiver(social_account_updated)
def signal_social_account_updated(sender, request, sociallogin, **kwargs):
    print('account updated')
    print(sociallogin.user)
    # update the user profile.
    # here, update everything that changed in the records.

