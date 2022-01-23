import logging
import os
from datetime import datetime, timedelta
from logging.config import dictConfig
from pathlib import Path
from typing import Optional

from django.conf import settings
from django.contrib.auth import authenticate
from django.core.asgi import get_asgi_application
from fastapi import Depends, FastAPI, HTTPException, Request, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.security.http import HTTPBasic, HTTPBasicCredentials
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from starlette.middleware import Middleware
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.responses import FileResponse
from starlette.routing import Mount

from starlette.staticfiles import StaticFiles
from starlette_prometheus import PrometheusMiddleware, metrics


from .logging_conf import LogConfig
from .auth import BasicAuthBackend

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Core.settings")

from Logic.routers import *


SECRET_KEY = os.environ.get("OAuth2Token")
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class User(BaseModel):
    username: Optional[str]


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


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


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(token: str = Depends(oauth2_scheme)):
    from Logic.models import UserModel

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = UserModel.objects.get(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


def get_current_active_user(current_user: User = Depends(get_current_user)):
    if not (current_user.is_active):
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


def setup_login(username, password):
    user = authenticate(username=username, password=password)
    return user


@fastapi.post("/login")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = setup_login(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username, "scopes": form_data.scopes},
        expires_delta=access_token_expires,
    )
    return {"access_token": access_token, "token_type": "bearer"}


@fastapi.get("/users/me/")
def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user.username


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


fastapi.add_middleware(PrometheusMiddleware)
fastapi.add_route("/metrics", metrics)
fastapi.include_router(user_router, prefix="/routes")
fastapi.include_router(issue_router, prefix="/issues_endpoint")
fastapi.include_router(admin_router, prefix="/administrator")
fastapi.include_router(comment_router, prefix="/comments")
