# -*- coding: utf-8 -*-
"""
Routes for API test project.
"""
from aiohttp import web


def setup_routes(app):
    """
    Setup project routes.

    :param app: Application
    """

    async def test(request):
        """
        Say hello to the API user.
        """
        return web.json_response(
            {
                "english": "Hello",
                "finnish": "Terve",
                "danish": "Hej",
                "swedish": "Hej",
                "lithuanian": "Sveiki",
                "russian": "Здравствуйте",
            }
        )

    app.add_routes([web.get("/", test)])
