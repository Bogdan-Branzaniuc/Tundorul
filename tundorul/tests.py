from django.test import TestCase
from tundorul.models import Vods, UserProfile
from suggestion.models import Suggestions
import datetime
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from tundorul.test_models import TestTundorul


class TestViews(TestTundorul):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

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
        self.assertEqual(response_approved_on_page.status_code, 200)
        self.assertTemplateUsed(response_approved_on_page, '/pending_approval.html')