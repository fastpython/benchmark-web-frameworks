# -*- coding: utf-8 -*-
from databases import Database


def setup_database(app):
    """
    Setup database for using Database.
    """
    app.db = Database(
        app.config.DB_URL,
        port=app.config.DB_PORT,
        database=app.config.DB_DATABASE,
        user=app.config.DB_USER,
        password=app.config.DB_PASSWORD,
    )

    @app.listener("after_server_start")
    async def connect_to_db(*args, **kwargs):
        await app.db.connect()

    @app.listener("after_server_stop")
    async def disconnect_from_db(*args, **kwargs):
        await app.db.disconnect()
