import lxml.html
import re

class Item(object):
    pass

class GeocachingScraper(object):
    def __init__(self, username):
        self.username = username
        self.tree = lxml.html.parse('http://www.geocaching.com/seek/nearest.aspx?ul='+self.username)
    
    def get_items(self):
        items = []
        cache_list = self.tree.xpath('//tr[@class="Data BorderTop"]')
        for cache in cache_list:
            item = Item()
            item.name = cache.xpath('td[6]/a/text()')[0]
            item.gc = re.search(r'.*\((GC[0-9A-Z]+)\)$', cache.xpath('td[6]/text()')[1]).group(1)
            item.url = 'http://coord.info/'+item.gc
            item.state = cache.xpath('td[6]/text()')[2].strip()
            items.append(item)
        return items
