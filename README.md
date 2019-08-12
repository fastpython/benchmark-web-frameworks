# Benchmark Python web frameworks

Repository for benchmarking and testing different Python frameworks and tools. Repository provides most simple setups for popular Python web frameworks to compare and test.

Included frameworks are:

- [Django](https://www.djangoproject.com/)
- [Flask](https://flask.palletsprojects.com)
- [Pyramid](https://trypyramid.com/)
- [Quart](https://pgjones.gitlab.io/quart/)
- [Sanic](https://github.com/huge-success/sanic)
- [Aiohttp](https://github.com/aio-libs/aiohttp/)

Don't run any of this code in production. This is for testing and benchmarking purposes only.


# Project setup

Each project has it's own environment stored in `Pipfile`s. You don't need to setup all projects, but just the one you want to test. Django setup is a bit different - more complex - than other frameworks. That's mostly Django is full-blown framework to handle everything and others used frameworks consider themselves as micro-frameworks.

Generally there are two requirements.

1. You'll need Python 3.6+
	- One option is to use [conda](https://docs.conda.io/en/latest/) for handling different Python versions
	- If you are not using Windows, there's also [pyenv](https://github.com/pyenv/pyenv) that you should consider
	- Or you can just download from [python.org](https://www.python.org/downloads/)

1. You also need [pipenv](https://github.com/pypa/pipenv)
	- For more details see documentation of [pipenv](https://docs.pipenv.org/en/latest/)
	- Or maybe example of [basic usage](https://docs.pipenv.org/en/latest/basics/)
	- Here's [exhaustive intro](https://realpython.com/pipenv-guide/) for why pipenv exists and should be used


## Django

[Django](https://www.djangoproject.com/) is *the* framework for Python web development if looking for a "batteries include" option. It has everything you need - especially if you don't know what you'll need. Django is opinionated. It'll provide suggestion for all parts of your web application. For some use cases, it is likely much more than you need, but it's still the most popular Python web framework there is.

To run Django project you need a few more commands than other frameworks - migrations. There's a reason other frameworks are called _micro_. They don't provide that much, but on the other hand you don't need to do that much setup procedures. In addition of requiring more commands there are also a few more files in the project compared to other frameworkds. They are mostly empty, but left there to remind user how Django would like to see the project structure.

Django is WSGI based and doesn't support the latest goods of `async/await`, but async support is listed as important part of [road map](https://www.aeracode.org/2018/06/04/django-async-roadmap/) in [DEP 0009](https://github.com/django/deps/blob/a7080e6f830815829fcee2f2b061f59bdeed489d/accepted/0009-async.rst). We'll see.

To run Django project:

1. Go to the test project folder root `fast-python/project-django`
1. Run `pipenv install` to install all dependencies
1. Move to Django project directory `fast-python/project-django/project`
1. Run migrations with `pipenv run python manage.py migrate`
1. Run `pipenv run python manage.py runserver` to run test server

And you'll find friendly _hello_ response from [http://127.0.0.1:8000](http://127.0.0.1:8000).

It's worth noting that migration steps above create SQLite database at project root (`fast-python/project-django/project`). Migrations you are running above are run agains that database. Assuming you don't change anything, you need to run migrations only once.


## Flask

If you know another Python web framework in addition to Django, it'll be most likely [Flask](https://github.com/pallets/flask/). Flask is a lightweight WSGI web application framework from [Pallets Projects](https://www.palletsprojects.com/). It began as a simple wrapper around [Werkzeug](https://www.palletsprojects.com/p/werkzeug/) and [Jinja](https://www.palletsprojects.com/p/jinja/) and has become one of the most popular Python web application frameworks. Now competing neck-to-neck with [Django](https://www.djangoproject.com/).

Compared to Django it's lightweight and not that opinionated on how different parts of the project should be done. [Documentation](https://flask.palletsprojects.com) is extensive and, since Flask is widely used, there are loads of tutorials to choose from if you want to get started with Flask.

To run Flask project:

1. Go to the test project folder root `fast-python/project-flask`
1. Run `pipenv install` to install all dependencies
1. Run `pipenv run python -m project` to run test server

And you'll find friendly _hello_ response from [http://0.0.0.0:8000](http://0.0.0.0:8000).


## Quart

[Quart](https://pgjones.gitlab.io/quart/) is a Python ASGI web microframework. It is intended to provide easy way to use asyncio functionality in a web context.

Important aspect of Quart is that the API is a superset of the Flask API. So, if you are using Flask and would like to test asyncio functionality, Quart is very good option. As [the documentation](https://pgjones.gitlab.io/quart/flask_migration.html) shows moving from Flask to Quart should be very straightforward.

To run Quart project:

1. Go to the test project folder root `fast-python/project-quart`
1. Run `pipenv install` to install all dependencies
1. Run `pipenv run python -m project` to run test server

And you'll find friendly _hello_ response from [http://0.0.0.0:8000](http://0.0.0.0:8000).


## Pyramid

[Pyramid](https://trypyramid.com/) is a framework that aims to hit between huge frameworks (i.e. Django) and smaller ones (i.e. Flask). Pyramid is nowhere near as popular if you read [Github stars](https://github.com/Pylons/pyramid), but is well liked when used. It's part of [Pylons project](https://pylonsproject.org/).

To run Pyramid project:

1. Go to the test project folder root `fast-python/project-pyramid`
1. Run `pipenv install` to install all dependencies
1. Run `pipenv run python -m project` to run test server

And you'll find friendly _hello_ response from [http://0.0.0.0:8000](http://0.0.0.0:8000).


## Sanic

[Sanic](https://github.com/huge-success/sanic) is a Python web framework built on uvloop and designed for fast HTTP responses via asynchronous request handling. It's currently one of the most popular ones of the few frameworks supporting asynchronous request handling - at least if you measure by Github stars.

Sanic framework is by default using [uvloop](https://magic.io/blog/uvloop-blazing-fast-python-networking/) for events and [ujson](https://pypi.org/project/ujson/) instead of standard json. That'll make it a bit faster than some other frameworks. So they say.

To run Sanic project:

1. Go to the test project folder root `fast-python/project-sanic`
1. Run `pipenv install` to install all dependencies
1. Run `pipenv run python -m project` to run test server

And you'll find friendly _hello_ response from [http://0.0.0.0:8000](http://0.0.0.0:8000).


## Aiohttp

[Aiohttp](https://github.com/aio-libs/aiohttp/) is asynchronous HTTP client/server framework for asyncio and Python. It's one of the more popular mini-frameworks supporting asynchronous request handling.

Key Features as they put it themselves:

- Supports both client and server side of HTTP protocol.
- Supports both client and server Web-Sockets out-of-the-box and avoids Callback Hell.
- Provides Web-server with middlewares and pluggable routing.

We don't use the client implementation in this repository, but it's nice to know that there would be one available if needed.

Framework has [good documentation](https://docs.aiohttp.org) and it's the best place to start when getting into the framework. Also the [list of demos](https://github.com/aio-libs/aiohttp-demos) is nice. The code in this repository is based on them.

To run Aiohttp project:

1. Go to the test project folder root `fast-python/project-aiohttp`
1. Run `pipenv install` to install all dependencies
1. Run `pipenv run python -m project` to run test server

And you'll find friendly _hello_ response from [http://0.0.0.0:8000](http://0.0.0.0:8000).


## Install pre-commit hooks

If you want to make changes for this repository you should have [pre-commit](https://pre-commit.com/) and related hooks installed as well. Easiest option is to install `pre-commit` and `black` directly to you "root" system. Some won't like it and there's no harm adding one more environment into the mix.

1. Go to repository root
1. Run `pip install pre-commit black` to install pre-commit
1. Run `pre-commit install` to install pre-commit hooks for the project

See detailed [pre-commit readme](README-pre-commit.md) for more details.


# Random notes

- Using [pre-commit]() to install Git pre-commit hooks and using [black](https://github.com/python/black) and flake8 to ensure commits are clean and nice.
- Details on pre-commit hooks and cleaning the code are in [readme-pre-commit.md](readme-pre-commit.md)
