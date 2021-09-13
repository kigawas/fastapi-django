# fastapi-django

FastAPI with Django ORM

More details are [here](https://kigawas.me/posts/integrate-fastapi-and-django-orm/).

## Directory hierarchy

```bash
$ tree -L 3 -I '__pycache__|venv|staticfiles' -P '*.py'
.
├── manage.py
├── mysite
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── polls
    ├── __init__.py
    ├── adapters
    │   └── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations
    │   ├── 0001_initial.py
    │   └── __init__.py
    ├── models
    │   └── __init__.py
    ├── routers
    │   ├── __init__.py
    │   ├── choices.py
    │   └── questions.py
    ├── schemas
    │   └── __init__.py
    └── tests.py

7 directories, 18 files
```

- `models`: Django ORMs
- `routers`: FastAPI routers
- `schemas`: Pydantic models
- `adapters`: Converting Django ORMs to Pydantic models

## Installation

```bash
poetry install
```

## Before the first run

### Migration

```bash
./manage.py migrate
```

### Data insertion

```bash
./manage.py shell
```

```python
>>> from polls.models import Choice, Question
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())
>>> q.save()
```

## Run

```bash
$ uvicorn mysite.asgi:fastapp --reload
...
$ ./manage.py collectstatic --noinput  # generate static files for django admin
...
$ uvicorn mysite.asgi:application --port 8001 --reload  # Django
...
$ curl http://localhost:8000/question/
{"items":[{"question_text":"What's new?","pub_date":"2021-03-29T04:18:54.724432+00:00"}]}%
```

### Mount Django asgi application

```python
# in mysite/settings.py

MOUNT_DJANGO_APP = True
```

Then http://localhost:8000/django/admin

## Tools

### FastAPI doc

```plaintext
http://localhost:8000/docs
```

### Django admin

```plaintext
http://localhost:8001/admin
```

### Pre-commit hook

```bash
pre-commit install
pre-commit run --all-files
```
