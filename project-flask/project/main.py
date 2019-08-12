# -*- coding: utf-8 -*-
from flask import Flask
from project.routes import setup_routes
from project.settings import Settings
from project.middlewares import setup_middlewares

# from project.database import setup_database


app = Flask(__name__)


def init():
    app.config.from_object(Settings)
    # setup_database(app)
    setup_routes(app)
    setup_middlewares(app)

    app.run(host=app.config["HOST"], port=app.config["PORT"])
