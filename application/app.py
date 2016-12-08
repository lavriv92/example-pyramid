import logging
from wsgiref.simple_server import make_server as wsgiref_server
from functools import wraps
from pyramid.config import Configurator


def make_server(host, port, app):
    return wsgiref_server(host, port, app)


class Application(object):
    def __init__(self):
        self.config = Configurator()

    def run(self, host='0.0.0.0', port=8080):
        app = self.config.make_wsgi_app()
        make_server(host, port, app).serve_forever()
        logging.info('App run on: http://%s:%s',  host, port)

    def route(self, route_path, name):
        def decorator(f):
            self.config.add_route(name, route_path)
            self.config.add_view(f, route_name=name)
        return decorator


app = Application()
