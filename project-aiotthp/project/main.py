# -*- coding: utf-8 -*-
from aiohttp import web
from project.routes import setup_routes
from project.middlewares import setup_middlewares
from project.database import setup_database
from project.settings import load_config


app = web.Application()


def init():
    app["config"] = load_config()
    setup_database(app)
    setup_routes(app)
    setup_middlewares(app)

    web.run_app(
        app=app, host=app["config"]["app"]["HOST"], port=app["config"]["app"]["PORT"]
    )
