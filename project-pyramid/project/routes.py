# -*- coding: utf-8 -*-
"""
Routes for API test project.
"""
from pyramid.response import Response


def setup_routes(config):
    """
    Setup project routes.

    :param app: Application
    """

    def test(request):
        """
        Say hello to the API user.
        """
        return Response(
            json={
                "english": "Hello",
                "finnish": "Terve",
                "danish": "Hej",
                "swedish": "Hej",
                "lithuanian": "Sveiki",
                "russian": "Здравствуйте",
            }
        )

    config.add_route("hello", "/")
    config.add_view(test, route_name="hello")
