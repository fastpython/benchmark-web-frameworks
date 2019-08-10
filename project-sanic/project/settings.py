# -*- coding: utf-8 -*-
"""
Project settings.
"""
from sanic_envconfig import EnvConfig


class Settings(EnvConfig):
    """
    Project settings and default values.
    """

    # Application settings
    DEBUG: bool = True
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # Database settings for PostgreSQL
    DB_URL: str = "localhost"
    DB_PORT: int = 5432
    DB_DATABASE: str = ""
    DB_USER: str = ""
    DB_PASSWORD: str = ""
