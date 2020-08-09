import tornado.httpserver
import tornado.web
import tornado.ioloop
from config_util import ConfigUtil

from core.handler import BaseHandler


class Application(tornado.web.Application):

    def __init__(self):
        print(type(BaseHandler))
        super(Application, self).__init__(handlers=[(r"/api/.*", BaseHandler)], debug=False)
        

if __name__ == '__main__':
    config = ConfigUtil(file_paths=[("server", "server.conf")])
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(int(config.get_config("server", "tornado", "port")))
    tornado.ioloop.IOLoop.instance().start()
