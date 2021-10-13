from fastapi import (
    APIRouter,
)
from fastapi.responses import HTMLResponse

user_router = APIRouter()


@user_router.get("/hello-world")
def Hello_world():
    return HTMLResponse("Hello World")
