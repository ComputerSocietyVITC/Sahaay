import os
from fastapi import FastAPI
from django.conf import settings
from starlette.staticfiles import StaticFiles
from starlette.routing import Mount
from django.core.asgi import get_asgi_application
from pathlib import Path
from starlette.responses import FileResponse
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Core.settings')

from Logic.routers import user_router

app = get_asgi_application()

DESIGN_DIR = str(Path(__file__).resolve().parent.parent.parent) + "\design\static"

if settings.MOUNT_DJANGO:
    routes: list = [
        Mount("/Master-Application", app),
        Mount("/static", StaticFiles(directory=DESIGN_DIR), name="static"),
    ]
    fastapi = FastAPI(routes=routes)

else:
    fastapi = FastAPI()

@fastapi.get("/favicon.ico")
def get_logo():
    path_to_file = str(Path(__file__).resolve().parent.parent.parent) + str("/design/logo/logo.svg")
    return FileResponse(path_to_file)

fastapi.include_router(user_router, prefix="/routes")