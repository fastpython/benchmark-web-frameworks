# Pre-commit hooks

Project is using [Pre-commit](https://github.com/pre-commit/pre-commit) project to setup Git pre-commit hooks for code cleaning and inspection.

- For more info on pre-commit package see [Pre-commit docs](https://pre-commit.com/)
- More info on Git pre-commit hooks see [official documentation](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) or this [shorted, but good introduction](https://githooks.com/)

Pre-commit setup in this project is based originally on this [blog post](https://ljvmiranda921.github.io/notebook/2018/06/21/precommits-using-black-and-flake8/). More checks and other stuff is added based on list at [Pre-commit docs](https://pre-commit.com/hooks.html).


### What are Git hooks?

Git hooks are scripts that Git executes before or after events such as: commit, push, and receive. Git hooks are a built-in feature - no need to download anything. Git hooks are run locally.


### How do Git hooks work?

Every Git repository has a `.git/hooks` folder with a script for each hook you can bind to. Developer can change or update these scripts as necessary, and Git will execute them when those events occur.

Congrid projects are using _pre-commit_ Python package that installs pre-commit hooks for your repository. It means that it creates the `.git/hooks` folder and adds scripts.

You could add more by yourself. The reason we are using _pre-commit_ package is that it's easy to keep hooks similar for all developers.


### Why should I care?

Git hooks can greatly increase your productivity as a developer. In Congrid projects they are used to:

- Reformat code to match [required formatting](https://github.com/python/black)
- Check code against [pep8](https://www.python.org/dev/peps/pep-0008/)
- Find errors from code
- Find bad code structure
- Look for [code smells](https://en.wikipedia.org/wiki/Code_smell)

# Install hooks

To setup Git pre-commit hooks you need to install pre-commit settings with:

```
pre-commit install
```

# Configure hooks

Hook settings are set in `.pre-commit-config.yaml`.

Currently pre-commit is set to run some pre-commit hooks, Black reformatting, pylint and flake8 checks. For the list of all supported hooks see [related documentation](https://pre-commit.com/hooks.html).


### Black

[Black](https://github.com/python/black) is the uncompromising Python code formatter. By using it, you agree to cede control over minutiae of hand-formatting. In return, Black gives you speed, determinism, and freedom from pycodestyle nagging about formatting. You will save time and mental energy for more important matters.

Not much config needed for Black. More details on Black see [documentation](https://github.com/python/black). There is no special settings file for Black, but it's just used as it's delievered.


### Flake8

[Flake8](https://gitlab.com/pycqa/flake8) is a Python tool that glues together pep8, pyflakes, mccabe, and third-party plugins to check the style and quality of some python code.

Flake8 is set to use 88 chars as back is using. For more details about that [88 chars](https://github.com/python/black#line-length) and for [configuring flake8](http://flake8.pycqa.org/en/2.6.0/config.html).

Flake8 settings are set in `setup.cfg`.
