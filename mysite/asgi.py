"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/asgi/
"""

import os

from django.conf import settings
from django.core.asgi import get_asgi_application
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

application = get_asgi_application()
fastapp = FastAPI()


def init(app: FastAPI):
    from polls.routers import register_routers

    register_routers(app)

    if settings.MOUNT_DJANGO_APP:
        app.mount("/django", application)  # type:ignore
        app.mount("/static", StaticFiles(directory="staticfiles"), name="static")


init(fastapp)
