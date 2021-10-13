from fastapi import (
    APIRouter,
    requests,
    Request,    
)
from fastapi.responses import HTMLResponse

userRouter = APIRouter()


@userRouter.get("/hello-world")
def Hello_world(request: Request):
    return HTMLResponse("Hello World")
