import tornado.web
import tornado.ioloop

class StacticRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class BasicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World!")


if __name__== "__main__":
    app = tornado.web.Application([
        (r"/", BasicRequestHandler),
        (r"/blog", StacticRequestHandler)
    ])
    app.listen(8881)
    tornado.ioloop.IOLoop.current().start()