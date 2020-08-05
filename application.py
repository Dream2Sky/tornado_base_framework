import tornado.httpserver
import tornado.web
import tornado.ioloop
from config_util import ConfigUtil


class Application(tornado.web.Application):

    def __init__(self):
        super(Application, self).__init__([], debug=True)
        

if __name__ == '__main__':
    config = ConfigUtil(file_paths=[("server", "server.conf")])
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(int(config.get_config("server", "tornado", "port")))
    tornado.ioloop.IOLoop.instance().start()
