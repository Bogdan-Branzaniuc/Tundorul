from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from allauth.socialaccount.models import SocialToken, SocialAccount
import requests
import json


class HandleVods(View):
    def get(self, request, *args, **kwargs):
        """

        """
        vods = [
            {'id': '1817207597', 'stream_id': '46852362636', 'user_id': '453874993', 'user_login': 'tundorul', 'user_name': 'Tundorul', 'title': '[PART 29] Ghost of Tsushima', 'description': '', 'created_at': '2023-05-11T16:28:06Z', 'published_at': '2023-05-11T16:28:06Z', 'url': 'https://www.twitch.tv/videos/1817207597', 'thumbnail_url': 'https://static-cdn.jtvnw.net/cf_vods/dgeft87wbj63p/211db826bfcbf075454f_tundorul_46852362636_1683822482//thumb/thumb0-%{width}x%{height}.jpg', 'viewable': 'public', 'view_count': 36, 'language': 'ro', 'type': 'archive', 'duration': '4h26m0s', 'muted_segments': None},
            {'id': '1816387533', 'stream_id': '46850149708', 'user_id': '453874993', 'user_login': 'tundorul', 'user_name': 'Tundorul', 'title': '[PART 28] Ghost of Tsushima', 'description': '', 'created_at': '2023-05-10T16:30:42Z', 'published_at': '2023-05-10T16:30:42Z', 'url': 'https://www.twitch.tv/videos/1816387533', 'thumbnail_url': 'https://static-cdn.jtvnw.net/cf_vods/dgeft87wbj63p/c336237ef5060f45ba6f_tundorul_46850149708_1683736238//thumb/thumb0-%{width}x%{height}.jpg', 'viewable': 'public', 'view_count': 17, 'language': 'ro', 'type': 'archive', 'duration': '1h25m30s', 'muted_segments': None},
            {'id': '1815549574', 'stream_id': '46848150380', 'user_id': '453874993', 'user_login': 'tundorul', 'user_name': 'Tundorul', 'title': '[PART 27] Ghost of Tsushima', 'description': '', 'created_at': '2023-05-09T16:29:43Z', 'published_at': '2023-05-09T16:29:43Z', 'url': 'https://www.twitch.tv/videos/1815549574', 'thumbnail_url': 'https://static-cdn.jtvnw.net/cf_vods/dgeft87wbj63p/dbb7351ac9232cbf5cf3_tundorul_46848150380_1683649776//thumb/thumb0-%{width}x%{height}.jpg', 'viewable': 'public', 'view_count': 42, 'language': 'ro', 'type': 'archive', 'duration': '2h11m30s', 'muted_segments': None},
            {'id': '1814728873', 'stream_id': '46846031580', 'user_id': '453874993', 'user_login': 'tundorul', 'user_name': 'Tundorul', 'title': '[PART 26] Ghost of Tsushima', 'description': '', 'created_at': '2023-05-08T16:30:21Z', 'published_at': '2023-05-08T16:30:21Z', 'url': 'https://www.twitch.tv/videos/1814728873', 'thumbnail_url': 'https://static-cdn.jtvnw.net/cf_vods/dgeft87wbj63p/7d714f05f6459735f03c_tundorul_46846031580_1683563416//thumb/thumb0-%{width}x%{height}.jpg', 'viewable': 'public', 'view_count': 27, 'language': 'ro', 'type': 'archive', 'duration': '2h54m0s', 'muted_segments': None},
            {'id': '1812084073', 'stream_id': '46838885500', 'user_id': '453874993', 'user_login': 'tundorul', 'user_name': 'Tundorul', 'title': '[PART 25] Ghost of Tsushima', 'description': '', 'created_at': '2023-05-05T16:30:29Z', 'published_at': '2023-05-05T16:30:29Z', 'url': 'https://www.twitch.tv/videos/1812084073', 'thumbnail_url': 'https://static-cdn.jtvnw.net/cf_vods/dgeft87wbj63p/81e57d96c9de63a610cb_tundorul_46838885500_1683304224//thumb/thumb0-%{width}x%{height}.jpg', 'viewable': 'public', 'view_count': 41, 'language': 'ro', 'type': 'archive', 'duration': '2h8m10s', 'muted_segments': None},
            {'id': '1811245746', 'stream_id': '46836770188', 'user_id': '453874993', 'user_login': 'tundorul', 'user_name': 'Tundorul', 'title': '[PART 24] Ghost of Tsushima', 'description': '', 'created_at': '2023-05-04T16:30:35Z', 'published_at': '2023-05-04T16:30:35Z', 'url': 'https://www.twitch.tv/videos/1811245746', 'thumbnail_url': 'https://static-cdn.jtvnw.net/cf_vods/dgeft87wbj63p/a7d9817d444127cb2ad7_tundorul_46836770188_1683217829//thumb/thumb0-%{width}x%{height}.jpg', 'viewable': 'public', 'view_count': 20, 'language': 'ro', 'type': 'archive', 'duration': '2h5m10s', 'muted_segments': None},
            {'id': '1810456575', 'stream_id': '46834714508', 'user_id': '453874993', 'user_login': 'tundorul', 'user_name': 'Tundorul', 'title': '[PART 23] Ghost of Tsushima', 'description': '', 'created_at': '2023-05-03T16:59:41Z', 'published_at': '2023-05-03T16:59:41Z', 'url': 'https://www.twitch.tv/videos/1810456575', 'thumbnail_url': 'https://static-cdn.jtvnw.net/cf_vods/dgeft87wbj63p/8f356c9627a14dc1825d_tundorul_46834714508_1683133176//thumb/thumb0-%{width}x%{height}.jpg', 'viewable': 'public', 'view_count': 24, 'language': 'ro', 'type': 'archive', 'duration': '2h4m50s', 'muted_segments': None},
            {'id': '1809587595', 'stream_id': '46832433452', 'user_id': '453874993', 'user_login': 'tundorul', 'user_name': 'Tundorul', 'title': '[PART 22] Ghost of Tsushima', 'description': '', 'created_at': '2023-05-02T16:30:45Z', 'published_at': '2023-05-02T16:30:45Z', 'url': 'https://www.twitch.tv/videos/1809587595', 'thumbnail_url': 'https://static-cdn.jtvnw.net/cf_vods/dgeft87wbj63p/a083f48200bd4ced346c_tundorul_46832433452_1683045040//thumb/thumb0-%{width}x%{height}.jpg', 'viewable': 'public', 'view_count': 15, 'language': 'ro', 'type': 'archive', 'duration': '2h12m40s', 'muted_segments': None},
]
        context = {
            'vods': vods
        }

        return render(
            request,
            'vods.html',
            context,
        )