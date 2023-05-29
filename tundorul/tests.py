from django.test import TestCase
from tundorul.models import Vods, UserProfile
import datetime


class TestViews(TestCase):

    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_refresh_vods(self):
        Vods.objects.create(
            id=1822284878,
            title='[Part 32] GoT - starting the DLC on Iki Island',
            url='https://www.twitch.tv/videos/1822284878',
            thumbnail_url='https://static-cdn.jtvnw.net/cf_vods/dgeft87w_168idth}x%{height}.jpg',
            published_at=datetime.datetime(2023, 5, 17, 26, 30, 11, tzinfo=None),
            view_count=1576,
            stream_id=12937432,
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