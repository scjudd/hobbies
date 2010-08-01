import lxml.html

class Item(object):
    pass

class DailyboothScraper(object):
    def __init__(self, username):
        self.username = username
    
    def get_items(self):
        items = []
        
        for index in lxml.html.parse('http://dailybooth.com/'+self.username).xpath('//li[@class="feed_picture"]'):
            detail = lxml.html.parse('http://dailybooth.com/'+index.xpath('div[1]/a[1]/@href')[0])
            
            item = Item()
            item.thumb_url = index.xpath('div[1]/a[1]/img/@src')[0]
            item.big_url = detail.xpath('//div[@id="picture"]/img/@src')[0]
            item.blurb = index.xpath('div[2]/div[2]/p/text()')
            items.append(item)
            
        return items
