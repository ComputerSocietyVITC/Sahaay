import os
from pathlib import Path

from django.conf import settings
from django.core.asgi import get_asgi_application

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

from starlette import middleware
from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.responses import FileResponse
from starlette.routing import Mount
from starlette.staticfiles import StaticFiles

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Core.settings")

from Logic.routers import user_router

from .auth import BasicAuthBackend

app = get_asgi_application()

DESIGN_DIR = str(Path(__file__).resolve().parent.parent.parent) + str(Path("design/static"))

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

middleware = [
    Middleware(AuthenticationMiddleware, backend = BasicAuthBackend)
]

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
    path_to_file = str(Path(__file__).resolve().parent.parent.parent) + str(
        "/design/logo/logo.svg"
    )
    return FileResponse(path_to_file)


fastapi.include_router(user_router,dependencies=[Depends(oauth2_scheme)] ,prefix="/routes")
