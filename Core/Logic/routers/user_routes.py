from typing import Optional

from django.contrib.auth import authenticate
from fastapi import APIRouter, Depends, Form, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from starlette import requests

user_router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="./token")


@user_router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    from Logic.models import UserModel

    user_data = UserModel.objects.filter(username=form_data.username)
    if not user_data:
        raise HTTPException(
            status_code = 417, detail="Incorrect User name, the query was not found"
        )

    user = authenticate(username = form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code = 400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}


@user_router.post("/form-handler/")
async def forms(username: str = Form(...), password: str = Form(...)):
    return {"username": username}


async def get_current_user(request):
    from Logic.models import UserModel
    user = UserModel.objects.filter(username = request.user)
    if not user:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

@user_router.get("/users/me")
async def read_users_me(request: Request):
    return (request.user)