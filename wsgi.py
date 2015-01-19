__author__ = 'Mouse'
import tornado.ioloop
import tornado.wsgi
import handlers
import settings as Settings

handlers = [
    (r'/', handlers.IndexHandler),
    (r'/manage', handlers.ManageHandler),
    (r'/postarticle', handlers.PostarticleHandler)
]


class Application(tornado.web.Application):
    def __init__(self):
        settings = dict(
            template_path=Settings.TEMPLATE_PATH,
            static_path=Settings.STATIC_PATH,
        )
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == '__main__':
    application = Application()
    print('Listening 8001...')
    application.listen(8001)
    tornado.ioloop.IOLoop.instance().start()
