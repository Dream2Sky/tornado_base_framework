import tornado.httpserver
import tornado.web
import tornado.ioloop


class Application(tornado.web.Application):

    def __init__(self):
        super(Application, self).__init__([], debug=True)

#TODO: 创建start函数用来启动， 并添加配置文件

if __name__ == '__main__':
    app = Application()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
