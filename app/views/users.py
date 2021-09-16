from fastapi import (
    APIRouter,
    Depends,
    status,
    HTTPException
)
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm

from json import JSONEncoder

from models.userModel import (
    UserModel,
    ValidateUserModel,
    UpdateUserModel,
    ShowUserModel
)

from views.dependencies import (
    hash_password,
    verify_password
)

from settings import db, ACCESS_TOKEN_EXPIRE_MINUTES

from typing import List
from datetime import datetime, timedelta

import re

class UserEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__

async def create_user(user: ValidateUserModel):
    if re.match("admin|dev|simple mortal", user.role):
        datetime_now = datetime.now()
        user.created_at = datetime_now.strftime("%m/%d/%y %H:%M:%S")
        user.password = hash_password(user.password)
        user = UserModel(user)
        user = jsonable_encoder(user)
        new_user = await db["users"].insert_one(user)
        created_user = await db["users"].find_one({"_id": new_user.inserted_id})
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_user)


    raise HTTPException(status_code=406, detail="User Role not acceptable")