#!/usr/bin/env python

import cherrypy
from mako.lookup import TemplateLookup

from scrapers.DailyboothScraper import DailyboothScraper
from scrapers.GeocachingScraper import GeocachingScraper

myDB = DailyboothScraper('scjudd')
myGC = GeocachingScraper('scjudd')

myLookup = TemplateLookup(directories=['.', 'templates'], output_encoding='utf-8', encoding_errors='replace')

class HomePage(object):
    def index(self):
        template = myLookup.get_template('index.html')
        return template.render(image_list = myDB.get_items()[:3])
    index.exposed = True

class DailyboothPage(object):
    def index(self):
        template = myLookup.get_template('dailybooth.html')
        return template.render(image_list = myDB.get_items())
    index.exposed = True

class GeocachingPage(object):
    def index(self):
        template = myLookup.get_template('geocaching.html')
        return template.render(cache_list = myGC.get_items())
    index.exposed = True


# Home page..
home =              HomePage()

# Dailybooth pages..
home.db =           DailyboothPage()
home.dailybooth =   DailyboothPage()

# Geocaching pages..
home.gc =           GeocachingPage()
home.geocaching =   GeocachingPage()

cherrypy.quickstart(home)
