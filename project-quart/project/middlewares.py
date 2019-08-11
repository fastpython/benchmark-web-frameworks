# -*- coding: utf-8 -*-
from secure import SecureHeaders

secure_headers = SecureHeaders()


def setup_middlewares(app):
    @app.after_request
    async def set_secure_headers(response):
        secure_headers.quart(response)
        return response
