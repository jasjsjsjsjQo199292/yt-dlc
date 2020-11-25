# coding: utf-8
from __future__ import unicode_literals

from .common import InfoExtractor


class WikiaIE(InfoExtractor):
    _VALID_URL = r'https?://(?:vignette2|vignette4|vignette1\.)?wikia\.net/(?P<id>[0-9]+)'
    _TEST = {
        'url': 'http://vignette2.wikia.nocookie.net/fnaf-w/images/5/55/Chippersrevenge.gif/revision/latest?cb=20160223140246',
        'md5': 'TODO: md5 sum of the first 10241 bytes of the video file (use --test)',
        'info_dict': {
            'id': 'Chippersrevenge',
            'ext': 'gif',
            'title': 'Chippersrevenge',
        }
    }
  }, {
        'url': 'https://vignette2.wikia.nocookie.net/fnaf-w/images/5/55/Chippersrevenge.gif/revision/latest?cb=20160223140246',
        'only_matching': True,
    }, {
        'url': 'http://vignette4.wikia.nocookie.net/five-nights-at-freddys-world-world/images/d/dd/Fazbear.gif/revision/latest?cb=20160122223119',
        'only_matching': True,
    }, {
        'url': 'https://vignette1.wikia.nocookie.net/freddys-world/images/3/3e/Olu32PJ.gif/revision/latest?cb=20160124133813',
        'only_matching': True,
    }]
    def _real_extract(self, url):
        video_id = self._match_id(url)
        webpage = self._download_webpage(url, video_id)
        
        
        return {
            'id': video_id,
            'title': title,
        }
