# Benchmark simple Python Web applications

Benchmarking and testing different Python frameworks and tools.

# Project setup

Each project has it's own environment stored in `Pipfile`s. You don't need to setup all projects, but just the one you want to test.

## Pre-setup

1. You'll need Python 3.6+
	- One option is to use [conda](https://docs.conda.io/en/latest/) for handling different Python versions
	- If you are not using Windows, there's also [pyenv](https://github.com/pyenv/pyenv) that you should consider
	- Or you can just download from [python.org](https://www.python.org/downloads/)
1. You also need [pipenv](https://github.com/pypa/pipenv)
	- For more details see documentation of [pipenv](https://docs.pipenv.org/en/latest/)
	- Or maybe example of [basic usage](https://docs.pipenv.org/en/latest/basics/)
	- Here's [exhaustive intro](https://realpython.com/pipenv-guide/) for why pipenv exists and should be used


## Test Sanic

Sanic project is originally based on this nice [blog article](https://medium.com/free-code-camp/goin-fast-and-asynchronous-with-python-and-sanic-387d722f3668). It's gives quick overview on Sanic.

1. Clone this repository
1. Go to the test project folder root `fast-python/sanic`
1. Run `pipenv install` to install all dependencies
1. Run `pipenv run python -m project` to run Sanic project test server

As a result you should see something like this:

```
$ pipenv install

Creating a virtualenv for this project…
Pipfile: /sanic/Pipfile
...
Installing dependencies from Pipfile.lock (668778)…
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 29/29 — 00:00:07
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.

$ pipenv run python -m project

Loading .env environment variables…
[2019-08-01 20:02:36 +0300] [2271] [DEBUG]

                 Sanic
         Build Fast. Run Fast.


[2019-08-01 20:02:36 +0300] [2271] [INFO] Goin' Fast @ http://0.0.0.0:8000
[2019-08-01 20:02:37 +0300] [2282] [INFO] Starting worker [2282]
```

And you'll find friendly _hello_ response from [http://0.0.0.0:8000](http://0.0.0.0:8000).


## Why care about Sanic?

Sanic is

- Sanic framework is by default using [uvloop](https://magic.io/blog/uvloop-blazing-fast-python-networking/) for events
- Sanic framework is by default using [ujson](https://pypi.org/project/ujson/) instead of standard json



## Install pre-commit hooks

If you want to make changes for this repository you should have [pre-commit](https://pre-commit.com/) and related hooks installed as well. Easiest option is to install `pre-commit` and `black` directly to you "root" system. Some won't like it and there's no harm adding one more environment into the mix.

1. Go to repository root
1. Run `pip install pre-commit black` to install pre-commit
1. Run `pre-commit install` to install pre-commit hooks for the project

See detailed [pre-commit readme](README-pre-commit.md) for more details.


## Notes

- Using [pre-commit]() to install Git pre-commit hooks and using [black](https://github.com/python/black) and flake8 to ensure commits are clean and nice.
- Details on pre-commit hooks and cleaning the code are in [readme-pre-commit.md](readme-pre-commit.md)
