# -*- coding: utf-8 -*-
"""
Project settings.
"""
import pathlib
import pytoml as toml

BASE_DIR = pathlib.Path(__file__).parent.parent
DEFAULT_CONFIG_PATH = BASE_DIR / "config" / "default.toml"
PACKAGE_NAME = "project-aiohttp"


def load_config(path=None):
    if not path:
        path = DEFAULT_CONFIG_PATH
    with open(path) as f:
        conf = toml.load(f)
    return conf
