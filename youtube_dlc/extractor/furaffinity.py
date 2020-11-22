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
                                                                      
        return {
            'id': video_id,
            'title': self._live_title(title) if is_live else title,
            'description': clean_html(media.get('description')),
           
            'duration': int_or_none(metadata.get('duration')) or None,
            'timestamp': int_or_none(metadata.get('created_time')),
            'uploader': owner.get('screenname'),
            'uploader_id': owner.get('id') or metadata.get('screenname'),
            'age_limit': 18 if metadata.get('explicit') else 0,
            'tags': metadata.get('tags'),
            'view_count': get_count('views') or int_or_none(media.get('audienceCount')),
           
            'formats': formats,
           
           
        }

