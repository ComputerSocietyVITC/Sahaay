from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm

from json import JSONEncoder

from models.userModel import (
    UserModel,
    ValidateUserModel,
    UpdateUserModel,
    ShowUserModel,
)

from views.dependencies import hash_password, verify_password

from settings import db, ACCESS_TOKEN_EXPIRE_MINUTES

from typing import List, Optional
from datetime import datetime, timedelta

import re


def json_encode(object):
    print(object)

    pass


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

        email = str(user["email"])

        if not (tst_user := await db["users"].find_one({"email": email})):
            new_user = await db["users"].insert_one(user)
        else:
            raise HTTPException(status_code=400, detail="User email already exists")
        created_user = await db["users"].find_one({"_id": new_user.inserted_id})
        return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_user)

    raise HTTPException(status_code=406, detail="User Role not acceptable")


async def update_user(user_id: str, user: UpdateUserModel):
    # if current_user["role"]=="admin" or str(current_user["_id"]) == user_id:
    user = {
        k: v
        for k, v in user.dict().items()
        if v is not None and k != "password_reverification"
    }
    if "password" in user.keys():
        user["password"] = hash_password(user["password"])

    if len(user) >= 1:
        update_result = await db["users"].update_one({"_id": user_id}, {"$set": user})
    if (
        update_result.modified_count == 1
        and (updated_user := await db["users"].find_one({"_id": user_id})) is not None
    ):
        return updated_user

    if (existing_user := await db["users"].find_one({"_id": user_id})) is not None:
        return existing_user

    raise HTTPException(status_code=404, detail=f"User {user_id} not found")
    # else:
    #     raise HTTPException(status_code=403, detail=f"Not having sufficient rights to modify the content")
    # pass


async def get_user(user_id: str):
    if (user := await db["users"].find_one({"_id": user_id})) is not None:
        return user
    raise HTTPException(status_code=404, detail=f"User {user_id} not found")


async def get_user_any_field(
    field_name: str, field_value: str, d_user: Optional[dict] = None
):
    if d_user is None:
        if field_value and field_value is not None:
            if user := await db["users"].find({field_name: field_value}).to_list(100):
                return user
        else:
            user = await db["users"].find().to_list(100)
            return user
    elif not (
        user := next((item for item in d_user if item[field_name] == field_value), None)
    ):
        return user
    raise HTTPException(status_code=404, detail=f"User not found")


async def delete_user(user_id: str):
    delete_result = await db["users"].delete_one({"_id": user_id})

    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"User {user_id} not found")
