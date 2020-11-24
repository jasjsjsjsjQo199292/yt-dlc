from __future__ import unicode_literals



from .common import InfoExtractor


class ShopifyIE(InfoExtractor)
     IE_NAME = 'shopify:gif' 
     _VALID_URL =  r'(?i)https?://(?:cdn\.)?shopify\.com/s/files/.*/(?P<id>[^/]+)/\w+(?:\.gif)?'
     _TESTS = [
        {
            'url': 'https://cdn.shopify.com/s/files/1/0344/6469/products/pizza-bed2_1024x1024.gif?v=1587691826',
               'info_dict': { 
                    'title': 'pizza-bed2_1024x1024',
                    'id': '1587691826',
                    'ext': 'gif'
                      }
                  
    def _real_extract(self, url):
        video_id = self._match_id(url)
        webpage = self._download_webpage(
            'https://cdn.shopify.com/s/files/'.format(id=video_id), video_id)

        width = int_or_none(self._og_search_property(
            'video:width', webpage, default=None))
        height = int_or_none(self._og_search_property(
            'video:height', webpage, default=None))

        video_elements = self._search_regex(
            r'(?s)<div class="video-elements">(.*?)</div>',
            webpage, 'video elements', default=None)
        if not video_elements:
            raise ExtractorError(
                'No sources found for video %s. Maybe an image?' % video_id,
                expected=True)

        formats = []
        for m in re.finditer(r'<source\s+src="(?P<src>[^"]+)"\s+type="(?P<type>[^"]+)"', video_elements):
            formats.append({
                'format_id': m.group('type').partition('/')[2],
                'url': self._proto_relative_url(m.group('src')),
                'ext': mimetype2ext(m.group('type')),
                'width': width,
                'height': height,
                'http_headers': {
                    'User-Agent': 'youtube-dlc (like wget)',
                },
            })

        gif_json = self._search_regex(
            r'(?s)var\s+videoItem\s*=\s*(\{.*?\})',
            webpage, 'GIF code', fatal=False)
        if gif_json:
            gifd = self._parse_json(
                gif_json, video_id, transform_source=js_to_json)
            formats.append({
                'format_id': 'gif',
                'preference': -10,
                'width': width,
                'height': height,
                'ext': 'gif',
                'acodec': 'none',
                'vcodec': 'gif',
                'container': 'gif',
                'url': self._proto_relative_url(gifd['gifUrl']),
                'filesize': gifd.get('size'),
                'http_headers': {
                    'User-Agent': 'youtube-dlc (like wget)',
                },
            })

        self._sort_formats(formats)

        return {
            'id': video_id,
            'formats': formats,
            'title': self._og_search_title(webpage, default=video_id),
        }

