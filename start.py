import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
# from pycket.session import SessionManager
from tornado.options import define, options
from urls import urlList
#zahradindar
define("port", default=1190, help="run on the given port", type=int)

# Your app launch code here..
class ALIEHApplication(tornado.web.Application):

    def __init__(self):
        # self.db = ["Medex"]
        handlers = urlListK
        settings = dict(
            debug=True,
            cookie_secret="61oETz3455545gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path= os.path.join(os.path.dirname(__file__), "static")


        )
        tornado.web.Application.__init__(self,handlers,**settings)

if __name__ == '__main__':
    tornado.options.parse_command_line()


    http_server = tornado.httpserver.HTTPServer(zahraApplication())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()