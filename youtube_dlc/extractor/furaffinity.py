# coding: utf-8
from __future__ import unicode_literals

import functools
import json
import re

from .common import InfoExtractor

from ..utils import (
    age_restricted)

class FuraffinityIE(InfoExtractor):
     _FAMILY_FILTER = None
     _VALID_URL = 'r'https?://(?:www\.)?furaffinity\.net/view/(?P<id>[^?#/]+)'
     _TEST = {
     'url': 'https://www.furaffinity.net/view/39326332/'
     'info_dict': {
          'id': '39326332',
          'ext': 'jpg' ,
          'title': '- Jumping coyote -',
          'description': '-',
          'uploader': 'dinych',
          'age_limit': '0',
          'upload_date': '20200822',
          },
        }, {
         'url': 'https://www.furaffinity.net/view/32332269/',
          'info_dict': {
          'id': '32332269',
          'ext': 'png',
          'title': 'Make a Wish',
          'description': '',
   !',
          'upload_date': '20190719'
          'uploader': 'PaceVanRign'
          'age_limit': '0'
          'view_count': 'int',
        },
        'skip': 'video gone',
         }, {
 # age-restricted
   'url': 'https://www.furaffinity.net/view/39326918/'
   'info_dict': {
            'id': '39326918',
            'ext': 'jpg',
            'title': 'Ych more reminder',
            'uploader': 'Puffic',
            'age_limit': '18',
        },
        'skip': 'video gone',
        }, {
        'url': 'https://www.furaffinity.net/view/19883645/',
        'only_matching': 'True',
        }
           
def _real_extract(self, url):
        media_id = self._match_id(url)
        formats = []
        uploader = None
        webpage = self._download_webpage(url, media_id)

        title = self._html_search_regex(
            r'<title>([^>]+)</title>', webpage, 'title')

        media_url_string = self._search_regex(
            r'"url"\s*:\s*("[^"]+"),', webpage, 'media url', default=None, fatal=False)

        if media_url_string:
            media_url = self._parse_json(media_url_string, media_id)
            formats = [{
                'url': media_url,
                'format_id': 'source',
                'quality': 1,
            }]
