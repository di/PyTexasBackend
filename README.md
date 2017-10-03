# PyTexasBackend

## Development Quickstart

Clone the repo:

```
git clone git@github.com:pytexas/PyTexasBackend.git
git submodule update --init
```

Create a venv and activate it:

```
$ python -m venv env
$ source env/bin/activate
```

Install the devlopment dependencies:

```
$ pip install -r requirements-dev.txt
$ npm install
```

Set up a minimum `.env` file:
```
$ echo "SECRET_KEY=an insecure development secret" > .env
```

Run unapplied migrations:

```
$ python manage.py migrate
```

Run the development server:
```
# backend
python manage.py runserver

# frontend
gulp watch
```

Add a dependency

```
# Python
pip-save install some-lib
```

Developing with a local frontend

```
# Some where outside the backend
git clone git@github.com:pytexas/PyTexas2017.git

export FRONTEND_DIR=/path/to/PyTexas2017
```
