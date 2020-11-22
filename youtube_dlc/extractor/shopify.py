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
                      
                      
                     
