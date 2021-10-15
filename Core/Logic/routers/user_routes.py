from typing import Optional

from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

user_router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

userRouter = APIRouter()

class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None
    
@userRouter.get("/hello-world")
def Hello_world(request: Request):
    print(list(request.user))
@user_router.get("/hello-world")
def Hello_world():
    return HTMLResponse("Hello World")


def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user

@userRouter.get("/items/")
async def read_items(current_user: User = Depends(get_current_user)):
    return current_user