__author__ = 'pardis32623410'
import tornado
from  models import *
import peewee
class newsHandler(tornado.web.RequestHandler):
     def get(self):
        newss =News.select()
        self.render('news.html', news = newss)
class newsEditHandler(tornado.web.RequestHandler):
     def get(self, *args):
       new_id=args[0]
       newInfo=News.select().where(News.id == new_id).get()
       self.render("news-edit.html",news=newInfo)

     def post(self, *args):
       new_id=args[0]
       newInfo = News.select().where(News.id == new_id).get()
       newInfo.title=self.get_argument("news-title")
       newInfo.body=self.get_argument("news-body")
       newInfo.date=self.get_argument("news-date")
       newInfo.category=self.get_argument("news-category")
       newInfo.author=self.get_argument("news-author")
       newInfo.save()


       self.redirect("/news")

class newsDeleteHandler(tornado.web.RequestHandler):
     def get(self, *args):
       new_id=args[0]
       newInfo = News.select().where(News.id ==new_id).get().delete_instance()
       self.redirect("/news")



class newsNewHandler(tornado.web.RequestHandler):
     def get(self, *args):
       self.render("news-new.html")


     def post(self, *args):

       cattitle = self.get_argument("news-title")
       catbody = self.get_argument("news-body")
       catdate = self.get_argument("news-date")
       catcategory = self.get_argument("news-category ")
       catauthor = self.get_argument("news-author")


       catInfo = News.create(
           title=cattitle,
           body=catbody,
           date=catdate,
           category=catcategory,
           author=catauthor

       )

       self.redirect("/news")
