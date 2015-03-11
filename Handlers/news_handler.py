__author__ = 'pardis32623410'
import tornado
from  models import *
import peewee
class newsHandler(tornado.web.RequestHandler):
     def get(self):
        news =News.select()
        self.render('news.html', categories = news)
