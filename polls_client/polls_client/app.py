import tornado.ioloop
import tornado.web
import urllib2


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        req = urllib2.Request('http://127.0.0.1:8000/api/hello', headers={'Content-Type': 'application/json'})
        res = urllib2.urlopen(req).read()
        self.write("Hello, world -----> %s " % res)

def make_app(port):
    return tornado.web.Application([
        (r"/", MainHandler),
    ], port=port)