# -*- coding: utf-8 -*-
from quart import Quart
from project.routes import setup_routes
from project.settings import Settings
from project.middlewares import setup_middlewares

# from project.database import setup_database


app = Quart(__name__)


def init():
    app.config.from_object(Settings)
    # setup_database(app)
    setup_routes(app)
    setup_middlewares(app)

    app.run(host=app.config["HOST"], port=app.config["PORT"], debug=app.config["DEBUG"])
