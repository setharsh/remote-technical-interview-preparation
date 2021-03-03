## What?
This is a simple project to test whether or not your system can use Poetry to install Python dependencies and successfully use one of those dependencies (`pytest`) in a Poetry-managed virtual environment.

## Prerequisites
* [Python](https://www.python.org/) `3.8` or greater
* [Poetry](https://python-poetry.org/) `0.12` or greater

## How?
```sh
poetry install --no-root && poetry run pytest --verbose
```

You should see a test run successfully.

## What Else?
This project makes as few assumptions as possible regarding your system, your choice of development environment, or anything else. Consult your development environment's documentation regarding how to configure it to use the virtual environment and dependencies managed by Poetry. Or don't. It's up to you.
