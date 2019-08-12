# -*- coding: utf-8 -*-
"""
Routes for API test project.
"""
from flask import jsonify


def setup_routes(app):
    """
    Setup project routes.

    :param app: Application
    """

    @app.route("/")
    def test():
        """
        Say hello to the API user.
        """
        return jsonify(
            {
                "english": "Hello",
                "finnish": "Terve",
                "danish": "Hej",
                "swedish": "Hej",
                "lithuanian": "Sveiki",
                "russian": "Здравствуйте",
            }
        )
