# -*- coding: utf-8 -*-
from aiohttp.web import middleware
from secure import SecureHeaders

secure_headers = SecureHeaders()


@middleware
async def set_secure_headers(request, handler):
    resp = await handler(request)
    secure_headers.aiohttp(resp)
    return resp


def setup_middlewares(app):
    app.middlewares.append(set_secure_headers)
