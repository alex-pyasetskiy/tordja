from app import make_app
from tornado.wsgi import WSGIAdapter

application = WSGIAdapter(make_app(8888))


