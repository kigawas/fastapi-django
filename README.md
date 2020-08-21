# fastapi-django
FastAPI with Django ORM

## Run

```bash
$ uvicorn mysite.asgi:fastapp --reload
$ uvicorn mysite.asgi:application --port 8001 --reload  # Django
$ curl http://localhost:8000/question/
```

## Doc

```
http://localhost:8000/docs
```

## Pre-commit hook

```bash
$ pre-commit install
$ pre-commit run --all-files
```
