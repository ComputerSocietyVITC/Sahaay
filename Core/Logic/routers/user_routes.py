from fastapi import APIRouter, Request
from pydantic.main import BaseModel
from pydantic.types import UUID4
import starlette
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND
from pydantic import EmailStr
user_router = APIRouter()


class PydanticUserModel(BaseModel):
    password: str
    username: str
    first_name: str
    last_name: str
    email: EmailStr
    Reg_no: str

class DeleteUserModel(BaseModel):
    Reg_no:str

@user_router.get("users/current-user")
async def current_user(request: Request):
    return request.user


@user_router.get("/all-users")
def show_all_users():
    from Logic.models import UserModel
    return list(UserModel.objects.values('Reg_no'))

@user_router.post("/user")
def create_user(user: PydanticUserModel):
    from Logic.models import UserModel
    pseudouser = UserModel(username = user.username, first_name = user.first_name, last_name = user.last_name, email = user.email, Reg_no=user.Reg_no)
    pseudouser.set_password(user.password)
    pseudouser.save()
    return f"User got created! {HTTP_201_CREATED}"

@user_router.delete("/user")
def delete_user(user: DeleteUserModel):
    from Logic.models import UserModel
    pseudouser = UserModel.objects.filter(Reg_no = user.Reg_no)
    if pseudouser:
        pseudouser.delete()
        return  f"The given user was deleted: {user.Reg_no}"
    else: 
        return f"User not found! HTTP {HTTP_404_NOT_FOUND}"

@user_router.put("/user")
def update_user(user: PydanticUserModel):
    from Logic.models import UserModel
    try:
        pseudouser = UserModel.objects.get(Reg_no = user.Reg_no)
        if pseudouser:
            pseudouser.first_name = user.first_name
            pseudouser.last_name = user.last_name
            pseudouser.email = user.email
            pseudouser.username = user.username
            pseudouser.save()
            return f"{pseudouser} was saved"
    except Exception:
            val = UserModel(username = user.username, first_name = user.first_name, last_name = user.last_name, email = user.email, Reg_no=user.Reg_no)
            val.save()
            return f"The user {val} was saved! HTTP {HTTP_200_OK}"

@user_router.get("/users/{user_id}")
def get_user(user_id: str):
    from Logic.models import UserModel
    user = UserModel.objects.filter(Reg_no=user_id)
    if user:
        return {"user":list(user)}
    else:
        return {"user": "empty"}
