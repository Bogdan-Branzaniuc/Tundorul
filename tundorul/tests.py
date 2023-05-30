from django.test import TestCase
from tundorul.models import Vods, UserProfile
from suggestion.models import Suggestions
import datetime
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class TestTundorul(TestCase):

    def create_and_login_user(self):
        '''
        testing Django User model along with tundorul UserProfile model,
        also starts and tests a login session for the created user.
        in the end returns the user and profile_user for further tests where access in pages is required
        '''
        User.objects.create_user(
            username='unittesting_user',
            password='unittesting_password',
            email='email@email.com',
        )
        user = get_object_or_404(User, username='unittesting_user')
        UserProfile.objects.create(
            username=user,
            uid=1234567,
            current_name='unittesting_user',
            email='unit@tests.com',
            join_date='2023-05-20',
            profile_picture_url='testUrl//http:8000',
        )
        self.client.force_login(user)
        logged_in_user_id = self.client.session.get('_auth_user_id')
        user_profile = get_object_or_404(UserProfile, username=user)

        self.assertIsNotNone(logged_in_user_id)
        self.assertEqual(int(logged_in_user_id), user.pk)
        self.assertEqual(user.username, 'unittesting_user')
        self.assertEqual(user_profile.username, user)
        return {
            'dj_user': user,
            'user_profile': user_profile,
        }

    def create_suggestion(self):
        user = self.create_and_login_user()
        Suggestions.objects.create(
            title='Test Title',
            body='Test Body',
            author=user['user_profile'],
        )
        suggestion = get_object_or_404(Suggestions, title='Test Title')
        return suggestion


    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_refresh_vods(self):
        '''
        Since The vods are updated every 6 hours with the latest 10 vods,
        the code is deletting all the vods and refilling the table with the request
        content, this way, if any data regarding the vods changed will also be updated
        '''

        Vods.objects.create(
            id=1,
            title='[Part 32] GoT - starting the DLC on Iki Island',
            url='https://www.twitch.tv/videos/1822284878',
            thumbnail_url='https://static-cdn.jtvnw.net/cf_vods/dgeft87w_168idth}x%{height}.jpg',
            published_at=datetime.datetime(2023, 5, 17, 16, 30, 11, tzinfo=None),
            view_count=1576,
            stream_id=11,
        )
        Vods.objects.create(
            id=2,
            title='Second Vod',
            url='https://www.twitch23123.tv/videos/1822284578',
            thumbnail_url='https:dth}x%{height}.jpg',
            published_at=datetime.datetime(2024, 5, 14, 16, 30, 1, tzinfo=None),
            view_count=991119,
            stream_id=22,
        )
        Vods.objects.all().delete()
        vod = Vods.objects.filter(title='[Part 32] GoT - starting the DLC on Iki Island')
        self.assertEqual(len(vod), 0)

        Vods.objects.create(
            id=123432141,
            title='Test Vod Is Here',
            url='https://www.twitch.tv/videos/1822284578',
            thumbnail_url='https://static-cdn.jtvnw.net/cf_vo4341006//thumb/thumb0-%{width}x%{height}.jpg',
            published_at=datetime.datetime(2023, 5, 17, 16, 30, 11, tzinfo=None),
            view_count=999,
            stream_id=1822284878,
        )
        vod = Vods.objects.filter(title='Test Vod Is Here')
        self.assertEqual(len(vod), 1)

    def test_get_vods_page(self):
        response = self.client.get('/vods')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vods.html')

    def test_get_login_if_not_page(self):
        response = self.client.get('/suggestions')
        response2 = self.client.get('/user_profile')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response2.status_code, 200)
        self.assertTemplateUsed(response, 'login_if_not.html')
        self.assertTemplateUsed(response2, 'login_if_not.html')

    def test_get_suggestions_profile_page(self):
        self.create_and_login_user()
        response = self.client.get('/suggestions')
        response2 = self.client.get('/user_profile')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response2.status_code, 200)
        self.assertTemplateUsed(response, 'suggestions.html')
        self.assertTemplateUsed(response2, 'user_profile.html')

    def test_add_suggestions(self):
        self.create_suggestion()
        suggestion = Suggestions.objects.filter(title='Test Title')
        self.assertEqual(len(suggestion), 1)

    def test_update_suggestions(self):
        self.test_add_suggestions()
        suggestion_update = get_object_or_404(Suggestions, title='Test Title')
        suggestion_update.title = 'updated_title'
        suggestion_update.save()
        self.assertEqual(suggestion_update.title, 'updated_title')

    def test_delete_suggestions(self):
        suggestion = self.create_suggestion()
        suggestion.delete()
        suggestion_count = Suggestions.objects.filter(title='Test Title').count()
        self.assertEqual(suggestion_count, 0)

    def test_get_404(self):
        response = self.client.get('/nonexistent-url')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')

    def test_get_banned_user_page_from_u_profile(self):
        user = self.create_and_login_user()
        user['user_profile'].is_banned = True
        user['user_profile'].save()
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/banned_user')

    def test_get_banned_user_page_from_v_page(self):
        user = self.create_and_login_user()
        user['user_profile'].is_banned = True
        user['user_profile'].save()
        response = self.client.get('/vods')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/banned_user')

    def test_get_banned_user_page_from_profile_page(self):
        user = self.create_and_login_user()
        user['user_profile'].is_banned = True
        user['user_profile'].save()
        response = self.client.get('/user_profile')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/banned_user')

    def test_get_banned_user_page_from_suggestions_page(self):
        user = self.create_and_login_user()
        user['user_profile'].is_banned = True
        user['user_profile'].save()
        response = self.client.get('/suggestions')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/banned_user')

    def test_user_profile_str_method(self):
        User.objects.create_user(
            username='unittesting_username_str',
            password='unittesting_password',
            email='email@email.com',
        )
        user = get_object_or_404(User, username='unittesting_username_str')
        user_profile = UserProfile.objects.create(
            username=user,
            uid=1234567,
            current_name='unittesting_user',
            email='unit@tests.com',
            join_date='2023-05-20',
            profile_picture_url='testUrl//http:8000',
        )
        self.assertEqual(str(user_profile), 'unittesting_user')

    def test_suggestions_str_method(self):
        author = self.create_and_login_user()['user_profile']
        suggestion = Suggestions.objects.create(
            title='Test Title',
            body='Test Body',
            author=author,
        )
        self.assertEqual(str(suggestion), 'Test Title')

    def test_vods_str_method(self):
        vod = Vods.objects.create(
            id=123432141,
            title='Test Vod Is Here',
            url='https://www.twitch.tv/videos/1822284578',
            thumbnail_url='https://static-cdn.jtvnw.net/cf_vo4341006//thumb/thumb0-%{width}x%{height}.jpg',
            published_at=datetime.datetime(2023, 5, 17, 16, 30, 11, tzinfo=None),
            view_count=999,
            stream_id=1822284878,
        )
        self.assertEqual(str(vod), 'Test Vod Is Here')

    def pending_approval_page_user_permissions_denied(self):
        user = self.create_and_login_user()
        response_denied = self.client.get('/pending_approval')
        self.assertEqual(response_denied.status_code, 200)
        self.assertTemplateUsed(response_denied, '/index.html')

    def pending_approval_page(self):
        user = self.create_and_login_user()
        user['dj_user'].staff_status = True
        user['dj_user'].superuser_status = True
        user['dj_user'].save()

        response_approved_on_page = self.client.get('/pending_approval')

        Suggestions.objects.create(
            title='Test1 Title1',
            body='Test1 Body1',
            author=user['user_profile'],
        )
        Suggestions.objects.create(
            title='Test2 Title2',
            body='Test2 Body2',
            author=user['user_profile'],
        )
        response_approved_suggestions = self.client.post({'title': 'Test2 Title2'})

        self.assertEqual(response_approved_suggestions, 200)
        self.assertTrue(user['dj_user'].is_staff)
        self.assertEqual(response_approved_on_page.status_code, 200)
        self.assertTemplateUsed(response_approved_on_page, '/pending_approval.html')