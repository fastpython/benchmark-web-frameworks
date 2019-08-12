# -*- coding: utf-8 -*-
from environs import Env
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from project.routes import setup_routes

# from project.middlewares import setup_middlewares


env = Env()
env.read_env()


def init():
    with Configurator() as config:
        setup_routes(config)
        # setup_middlewares(config)
        app = config.make_wsgi_app()
    server = make_server(env("HOST"), int(env("PORT")), app)
    server.serve_forever()
