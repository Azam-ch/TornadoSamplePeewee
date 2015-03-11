__author__ = 'mojtaba.banaie'
from Handlers.index_handler import IndexHandler
from Handlers.category__handler import CategoryHandler,CategoryEditHandler,CategoryDeleteHandler,CategoryNewHandler

urlList  = [
    (r'/', IndexHandler),
    (r'/category$', CategoryHandler),
    (r'/category/edit/(\d+)$', CategoryEditHandler),
    (r'/category/delete/(\d+)$', CategoryDeleteHandler),
    (r'/category/new$', CategoryNewHandler),

    (r'/news$', newsHandler),
    (r'/news/edit/(\d+)$', nessEditHandler),
    (r'/news/delete/(\d+)$', newsDeleteHandler),
    (r'/news/new$', newsNewHandler),


]