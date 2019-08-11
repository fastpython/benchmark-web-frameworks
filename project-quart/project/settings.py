# -*- coding: utf-8 -*-
"""
Project settings.
"""
from environs import Env


env = Env()
env.read_env()


class Settings(object):
    """
    Project settings and default values.
    """

    # Application settings
    DEBUG: bool = env("DEBUG", True)
    HOST: str = env("HOST", "0.0.0.0")
    PORT: int = env("PORT", 8000)

    # Database settings for PostgreSQL
    DB_URL: str = env("DB_URL", "localhost")
    DB_PORT: int = env("DB_PORT", 5432)
    DB_DATABASE: str = env("DB_DATABASE", "test_database")
    DB_USER: str = env("DB_USER", "test_user")
    DB_PASSWORD: str = env("DB_PASSWORD", "test_password")
