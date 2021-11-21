from fastapi import APIRouter, Request
from pydantic.main import BaseModel
from pydantic.types import UUID4
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND
from pydantic import EmailStr

from .abstraction import create_user_model, patch_user_model

user_router = APIRouter()


class PydanticUserModel(BaseModel):
    password: str
    username: str
    first_name: str
    last_name: str
    email: EmailStr
    Reg_no: str


class DeleteUserModel(BaseModel):
    Reg_no: str


@user_router.get("/users/current-user")
async def current_user(request: Request):
    return request.user


@user_router.get("/all-users")
def show_all_users(request: Request):
    from Logic.models import UserModel

    if request.user.is_authenticated:
        return list(UserModel.objects.values("Reg_no"))


@user_router.post("/user")
def create_user(request: Request, user: PydanticUserModel):
    from Logic.models import UserModel

    if request.user.is_authenticated and UserModel.objects.get(
        username=request.user.username
    ):
        create_user_model(user)
        return {HTTP_201_CREATED:f"{user}"}


@user_router.delete("/user")
def delete_user(request: Request, user: DeleteUserModel):
    from Logic.models import UserModel

    pseudouser = UserModel.objects.filter(Reg_no=user.Reg_no)
    if pseudouser and UserModel.objects.get(username=request.user.username).is_staff:
        if request.user.is_authenticated and UserModel.objects.get(
            username=request.user.username
        ):
            pseudouser.delete()
            return {HTTP_200_OK:user.Reg_no}
    else:
        return HTTP_404_NOT_FOUND


@user_router.patch("/user")
def update_user(request: Request, user: PydanticUserModel):
    from Logic.models import UserModel
    pseudouser = UserModel.objects.get(Reg_no=user.Reg_no)
    if pseudouser and (
        request.user.username == pseudouser.username
        or UserModel.objects.get(username=request.user.username).is_staff
    ):
        patch_user_model(pseudouser, user)
    return {HTTP_200_OK:f"pseudouser"}


@user_router.get("/user/{user_id}")
def get_specific_user(user_id: str):
    from Logic.models import UserModel

    pseudouser = UserModel.objects.filter(Reg_no=user_id)
    return list(pseudouser)
