from django.contrib.auth import authenticate
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.security import HTTPBasicCredentials
from fastapi.security.http import HTTPBasic

user_router = APIRouter()
security = HTTPBasic()


@user_router.post("/login")
def login(
    request: Request, credentials: HTTPBasicCredentials = Depends(security)
):
    from Logic.models import UserModel

    user_data = UserModel.objects.filter(username=credentials.username)
    if not user_data:
        raise HTTPException(
            status_code=417, detail="Incorrect User name, the query was not found"
        )

    user = authenticate(username=credentials.username, password=credentials.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    if user and request.method == "POST":
        return request.headers


@user_router.get("/users/me")
async def read_users_me(request: Request):
    return request.user
