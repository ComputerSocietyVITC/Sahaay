from fastapi import (
    APIRouter,
    Depends,
    status,
    HTTPException
)
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm

from settings import db

from views.users import (
    create_user
)

from models.userModel import (
    ValidateUserModel,
    UserModel,
    UpdateUserModel,
    ShowUserModel
)

router = APIRouter()

@router.post("/user", response_description="Add new user", response_model=ValidateUserModel)
async def create_user(user:UserModel = Depends(create_user)):
    return user
