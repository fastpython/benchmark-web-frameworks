# -*- coding: utf-8 -*-
"""
Routes for API test project.
"""
from sanic.response import json


def setup_routes(app):
    """
    Setup project routes.

    :param app: Application
    """

    @app.route("/")
    async def test(request):
        """
        Say hello to the API user.
        """
        return json(
            {
                "english": "Hello",
                "finnish": "Terve",
                "danish": "Hej",
                "swedish": "Hej",
                "lithuanian": "Sveiki",
                "russian": "Здравствуйте",
            }
        )
