# -*- coding: utf-8 -*-
from databases import Database


def setup_database(app):
    """
    Setup database for using Database.
    """
    app["db"] = Database(
        app["config"]["db"]["DB_URL"],
        port=app["config"]["db"]["DB_PORT"],
        database=app["config"]["db"]["DB_DATABASE"],
        user=app["config"]["db"]["DB_USER"],
        password=app["config"]["db"]["DB_PASSWORD"],
    )

    async def connect_to_db(*args, **kwargs):
        await app["db"].connect()

    async def disconnect_from_db(*args, **kwargs):
        await app["db"].disconnect()

    app.on_startup.append(connect_to_db)
    app.on_cleanup.append(disconnect_from_db)
