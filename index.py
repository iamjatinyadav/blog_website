import tornado.web
import tornado.ioloop

class BasicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World!")


if __name__== "__main__":
    app = tornado.web.Application([
        (r"/", BasicRequestHandler)
    ])
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()