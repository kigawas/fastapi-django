# fastapi-django

FastAPI with Django ORM

## Folder hierarchy

```bash
$ tree -L 3 -I '__pycache__|venv|staticfiles' -P '*.py'
.
├── manage.py
├── mysite
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── polls
    ├── __init__.py
    ├── adapters
    │   └── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations
    │   ├── 0001_initial.py
    │   └── __init__.py
    ├── models
    │   └── __init__.py
    ├── routers
    │   └── __init__.py
    ├── schemas
    │   └── __init__.py
    └── tests.py

7 directories, 16 files
```

- `models`: Django ORMs
- `routers`: FastAPI routers
- `schemas`: Pydantic models
- `adapters`: Converting Django ORMs to Pydantic models

## Run

```bash
$ ./manage.py migrate
...
$ uvicorn mysite.asgi:fastapp --reload
...
$ uvicorn mysite.asgi:application --port 8001 --reload  # Django
...
$ curl http://localhost:8000/question/

{"items":[]}%
```

## Doc

```plaintext
http://localhost:8000/docs
```

## Pre-commit hook

```bash
pre-commit install
pre-commit run --all-files
```
