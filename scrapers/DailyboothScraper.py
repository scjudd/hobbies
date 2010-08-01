import lxml.html

class Item(object):
    pass

class DailyboothScraper(object):
    def __init__(self, username):
        self.username = username
        self.tree = lxml.html.parse('http://dailybooth.com/'+self.username)
    
    def get_items(self):
        items = []
        image_list = self.tree.xpath('//li[@class="feed_picture"]')
        for image in image_list:
            item = Item()
            item.url = image.xpath('div[1]/a[1]/img/@src')[0]
            item.blurb = image.xpath('div[2]/div[2]/p/text()')[0]
            items.append(item)
        return items