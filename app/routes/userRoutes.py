from typing import Optional
from settings import ACCESS_TOKEN_EXPIRE_MINUTES

from datetime import timedelta

from views.dependencies import authenticate_user, get_current_user
from fastapi import (
    APIRouter,
    Depends,
    status,
    HTTPException
)

from fastapi.security import OAuth2PasswordRequestForm

from settings import db

from views.users import (
    create_user, update_user, get_user, get_user_any_field,
    delete_user
)

from views.dependencies import (
    create_access_token, get_current_user
)

from models.userModel import (
    ValidateUserModel,
    UserModel,
    UpdateUserModel,
    ShowUserModel
)

from datetime import datetime, timedelta

userRouter = APIRouter()

@userRouter.get("/user/get_one",response_description="Get user by id", response_model= ShowUserModel)
async def get_user_route(user_id: str):
    return await get_user(user_id)

@userRouter.get("/user/get_query",response_description="Get user by query")
async  def get_user_query_route(field_name: Optional[str]=None, field_value:Optional[str]=None, d_user:Optional[dict]=None):
    return await  get_user_any_field(field_name, field_value, d_user)

@userRouter.get("/current", response_description="Current user", response_model=ShowUserModel)
async def current_user_route(current_user: ShowUserModel = Depends(get_current_user)):
    return current_user


@userRouter.post("/user", response_description="Add new user", response_model=ValidateUserModel)
async def create_user_route(user:UserModel = Depends(create_user)):
    return user

@userRouter.post("/token", response_description="Login User")
async def login_route(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect ID or Password",
            headers={"WWW-Authenticate":"Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user['email']}, expires_delta=access_token_expires
    )
    await db["users"].update_one({'email': form_data.username}, {"$set": {
        "last_login": datetime.now().strftime("%m/%d/%y %H:%M:%S"),
        "is_active": "true"
    }})
    
    return {"access_token":access_token, "token_type":"bearer"}

@userRouter.patch("/user/update",response_description="Update existing user", response_model= UpdateUserModel)
async def update_user_route(user: UpdateUserModel,user_id: Optional[str]=None, email:Optional[str]=None):
    if user_id is None and email is not None:
        _ = await get_user_any_field("email",email)
        user_id = _[0]["_id"]
    updated_user = await update_user(user_id, user)
    return updated_user
    
@userRouter.delete("/user/delete", response_description="Deleted user")
async def delete_user_route(res = Depends(delete_user)):
    return res