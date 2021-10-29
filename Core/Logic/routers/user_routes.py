from fastapi import APIRouter,Request

user_router = APIRouter()



@user_router.get("/users/me")
async def read_users_me(request: Request):
    return request.user
