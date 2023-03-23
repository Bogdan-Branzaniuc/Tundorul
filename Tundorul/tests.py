from django.test import TestCase
from .models import UserProfile

from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialApp, SocialAccount
from django.shortcuts import render, get_object_or_404, reverse


class TestSocialAccount(TestCase):
    def test_match_social_account(self):

        app = SocialApp.objects.create(provider='twitch',
                                       name='Twitch',
                                       client_id='hf3ftyp7rubp7kdu4ebr7fy0flzba8',
                                       secret='boxcbhf9h2yhd1vqhh39xiqh7xs69c')

        user_instance = User.objects.create(username='notonuclearwar', email='bbranzaniuc53@gmail.com', first_name='notonuclearwar')

        account = SocialAccount.objects.create(user=user_instance,
                                               provider='twitch',
                                               uid='753993152',
                                               extra_data={"id": "753993152", "login": "notonuclearwar", "display_name": "notonuclearwar", "type": "", "broadcaster_type": "", "description": "", "profile_image_url": "https://static-cdn.jtvnw.net/jtv_user_pictures/a7ce3358-5ebe-404d-88ae-45c493fd558a-profile_image-300x300.png", "offline_image_url": "", "view_count": 0, "email": "bbranzaniuc53@gmail.com", "created_at": "2021-12-19T08:34:36Z"},
                                               app=app)


        user_profile = UserProfile.objects.create(
            user=user_instance,
            uid=account.extra_data['id'],
            current_name=account.extra_data['display_name'],
            email=account.extra_data['email'],
            time_watched=999999,
            channel_points=150,
            is_subscribed=True,
            subscribed_since=99999,
        )
        user_profile.commit()
        user_profile.save()

        user_data = get_object_or_404(UserProfile, social_account=account)

        self.assertEqual(user_data.uid, 753993152)

