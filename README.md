# Benchmark simple Python Web applications

Benchmarking and testing different Python frameworks and tools.

# Project setup

Each project has it's own environment stored in `Pipfile`s. You don't need to setup all projects, but just the one you want to test.

1. You'll need Python 3.6+
	- One option is to use [conda](https://docs.conda.io/en/latest/) for handling different Python versions
	- If you are not using Windows, there's also [pyenv](https://github.com/pyenv/pyenv) that you should consider
	- Or you can just download from [python.org](https://www.python.org/downloads/)
1. You also need [pipenv](https://github.com/pypa/pipenv)
	- For more details see documentation of [pipenv](https://docs.pipenv.org/en/latest/)
	- Or maybe example of [basic usage](https://docs.pipenv.org/en/latest/basics/)
	- Here's [exhaustive intro](https://realpython.com/pipenv-guide/) for why pipenv exists and should be used


## Flask

If you have read anything about web development then you must know [Flask](https://github.com/pallets/flask/). Flask is a lightweight WSGI web application framework from [Pallets Projects](https://www.palletsprojects.com/). It began as a simple wrapper around [Werkzeug](https://www.palletsprojects.com/p/werkzeug/) and [Jinja](https://www.palletsprojects.com/p/jinja/) and has become one of the most popular Python web application frameworks. Now competing neck-to-neck with [Django](https://www.djangoproject.com/)

Compared to Django it's lightweight and not that opinionated on how different parts of the project should be done. [Documentation](https://flask.palletsprojects.com) is extensive and, since Flask is widely used, there are loads of tutorials to choose from if you want to get started with Flask.

To run Flask project:

1. Go to the test project folder root `fast-python/project-flask`
1. Run `pipenv install` to install all dependencies
1. Run `pipenv run python -m project` to run Sanic project test server

And you'll find friendly _hello_ response from [http://0.0.0.0:8000](http://0.0.0.0:8000).


## Quart

[Quart](https://pgjones.gitlab.io/quart/) is a Python ASGI web microframework. It is intended to provide easy way to use asyncio functionality in a web context.

Important point is that the Quart API is a superset of the Flask API. So, if you are using Flask and would like to test asyncio functionality, Quart is very good option. As [the documentation](https://pgjones.gitlab.io/quart/flask_migration.html) shows moving from Flask to Quart should be very straightforward.

To run Quart project:

1. Go to the test project folder root `fast-python/project-quart`
1. Run `pipenv install` to install all dependencies
1. Run `pipenv run python -m project` to run Sanic project test server

And you'll find friendly _hello_ response from [http://0.0.0.0:8000](http://0.0.0.0:8000).


## Sanic

Sanic project is originally based on this nice [blog article](https://medium.com/free-code-camp/goin-fast-and-asynchronous-with-python-and-sanic-387d722f3668). It's gives quick overview on Sanic.

To run Sanic project:

1. Go to the test project folder root `fast-python/project-sanic`
1. Run `pipenv install` to install all dependencies
1. Run `pipenv run python -m project` to run Sanic project test server

And you'll find friendly _hello_ response from [http://0.0.0.0:8000](http://0.0.0.0:8000).

Sanic is

- Sanic framework is by default using [uvloop](https://magic.io/blog/uvloop-blazing-fast-python-networking/) for events
- Sanic framework is by default using [ujson](https://pypi.org/project/ujson/) instead of standard json


## Aiohttp

[Aiohttp](https://github.com/aio-libs/aiohttp/) is asynchronous HTTP client/server framework for asyncio and Python. It's one of the more popular mini-frameworks supporting asynchronous request handling.

Key Features as they put it themselves:

- Supports both client and server side of HTTP protocol.
- Supports both client and server Web-Sockets out-of-the-box and avoids Callback Hell.
- Provides Web-server with middlewares and pluggable routing.

We don't use the client implementation in this framework, but it's nice to that there would be one available if needed.

Framework has [good documentation](https://docs.aiohttp.org) and it's the best place to start when getting into the framework. Also the [list of demos](https://github.com/aio-libs/aiohttp-demos) is nice. The code in this repository is based on them.

To run Aiohttp project:

1. Go to the test project folder root `fast-python/project-aiohttp`
1. Run `pipenv install` to install all dependencies
1. Run `pipenv run python -m project` to run Sanic project test server

And you'll find friendly _hello_ response from [http://0.0.0.0:8000](http://0.0.0.0:8000).



## Install pre-commit hooks

If you want to make changes for this repository you should have [pre-commit](https://pre-commit.com/) and related hooks installed as well. Easiest option is to install `pre-commit` and `black` directly to you "root" system. Some won't like it and there's no harm adding one more environment into the mix.

1. Go to repository root
1. Run `pip install pre-commit black` to install pre-commit
1. Run `pre-commit install` to install pre-commit hooks for the project

See detailed [pre-commit readme](README-pre-commit.md) for more details.


## Notes

- Using [pre-commit]() to install Git pre-commit hooks and using [black](https://github.com/python/black) and flake8 to ensure commits are clean and nice.
- Details on pre-commit hooks and cleaning the code are in [readme-pre-commit.md](readme-pre-commit.md)
