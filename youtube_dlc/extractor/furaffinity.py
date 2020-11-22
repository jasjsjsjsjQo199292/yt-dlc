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
          'description': 'Feral fullbody for:MrSilverFox 
I am having sooooo much fun with these. Does it show? Because they seriously just
fill me with happiness every single time! I
definitely plan to open for more in the future!',
          'upload_date': 20190719
          'uploader': PaceVanRign
          'age_limit': '0'
          'view_count': int,
        },
        'skip': 'video gone',
         }, {
 # age-restricted
   'url': https://www.furaffinity.net/view/39326918/
   'info_dict': {
            'id': '39326918',
            'ext': 'jpg',
            'title': 'Ych more reminder',
            'uploader': 'Puffic',
            'age_limit': 18,
        },
        'skip': 'video gone',
        }, {
        'url': 'https://www.furaffinity.net/view/19883645/',
        'only_matching': True,
        }
        

