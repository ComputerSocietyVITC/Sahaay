from fastapi import (
    APIRouter,
)
from fastapi.responses import HTMLResponse

userRouter = APIRouter()


@userRouter.get("/hello-world")
def Hello_world():
    return HTMLResponse("Hello World")
