from typing import Optional

from django.contrib.auth import authenticate
from fastapi import APIRouter, Depends, Form, HTTPException, requests
from fastapi.responses import HTMLResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

user_router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="./token")


@user_router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    from Logic.models import UserModel

    user_data = UserModel.objects.filter(username=form_data.username)
    if not user_data:
        raise HTTPException(
            status_code=417, detail="Incorrect User name, the query was not found"
        )

    user = authenticate(username=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}


@user_router.post("/form-handler/")
async def forms(username: str = Form(...), password: str = Form(...)):
    return {"username": username}


@user_router.get("/current-user")
def return_current_user(request):
    return request.user
