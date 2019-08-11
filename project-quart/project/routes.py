# -*- coding: utf-8 -*-
"""
Routes for API test project.
"""
from quart import jsonify


def setup_routes(app):
    """
    Setup project routes.

    :param app: Application
    """

    @app.route("/")
    async def test():
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
