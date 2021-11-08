import logging
import os
from logging.config import dictConfig
from pathlib import Path

from django.conf import settings
from django.contrib.auth import authenticate
from django.core.asgi import get_asgi_application
from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.security.http import HTTPBasic, HTTPBasicCredentials
from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.responses import FileResponse
from starlette.routing import Mount
from starlette.staticfiles import StaticFiles

from .logging_conf import LogConfig

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Core.settings")

from Logic.routers import (admin_router, comment_router, issue_router,
                           user_router)

from .auth import BasicAuthBackend


dictConfig(LogConfig().dict())
logger = logging.getLogger("sahaay_app")

security = HTTPBasic()
app = get_asgi_application()

DESIGN_DIR = str(Path(__file__).resolve().parent.parent.parent) + str(
    Path(r"/design/static")
)


middleware = [Middleware(AuthenticationMiddleware, backend=BasicAuthBackend())]

if settings.MOUNT_DJANGO:
    routes: list = [
        Mount("/Master-Application", app),
        Mount("/static", StaticFiles(directory=DESIGN_DIR), name="static"),
    ]
    fastapi = FastAPI(routes=routes, middleware=middleware)

else:
    fastapi = FastAPI(middleware=middleware)


@fastapi.get("/favicon.ico")
def get_logo():
    path_to_file = str(Path(__file__).resolve().parent.parent.parent) + str(
        "/design/logo/logo.svg"
    )
    return FileResponse(path_to_file)


@fastapi.get("/login")
def login(request: Request, credentials: HTTPBasicCredentials = Depends(security)):
    from Logic.models import UserModel

    user_data = UserModel.objects.filter(username=credentials.username)
    if not user_data:
        raise HTTPException(
            status_code=417, detail="Incorrect User name, the query was not found"
        )

    user = authenticate(username=credentials.username, password=credentials.password)
    if not user:
        logger.error("Authentication Error")
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    # if user and request.method == "POST":
    #     return request.user


fastapi.include_router(user_router, prefix="/routes")
fastapi.include_router(issue_router, prefix="/issues_endpoint")
fastapi.include_router(admin_router, prefix="/administrator")
fastapi.include_router(comment_router, prefix="/comments")