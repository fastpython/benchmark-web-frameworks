# -*- coding: utf-8 -*-
from django.http import JsonResponse


def test(request):
    """
    Say hello to the API user.
    """
    return JsonResponse(
        {
            "english": "Hello",
            "finnish": "Terve",
            "danish": "Hej",
            "swedish": "Hej",
            "lithuanian": "Sveiki",
            "russian": "Здравствуйте",
        }
    )
