from django.test import TestCase


class TestViews(TestCase):

    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_add_suggestions(self):
        pass

    def test_refresh_vods(self):
        pass

    def test_get_vods_page(self):
        pass

    def test_get_vods(self):
        pass

    def test_create_user_profile(self):
        pass

    def test_get_user_profile(self):
        pass

    def test_get_suggestions(self):
        pass

    def test_delete_suggestions(self):
        pass