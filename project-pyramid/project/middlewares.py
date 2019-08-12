# -*- coding: utf-8 -*-
from secure import SecureHeaders

secure_headers = SecureHeaders()


def setup_middlewares(config):
    def set_secure_headers(handler, registry):
        def tween(request):
            response = handler(request)
            secure_headers.pyramid(response)
            return response

        return tween

    config.add_tween("set_secure_headers")
