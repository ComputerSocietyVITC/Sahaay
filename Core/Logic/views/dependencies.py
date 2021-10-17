# Can be scrapped, this basically deals with the enocding and auth middleware using fastAPi, 
# but since Django handles that for us, we can scrap all the code here
# not making any changes by myself so as to not break the code


from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from Core.app_secrets import pwd_context, db, oauth2_scheme, SECRET_KEY, ALGORITHM

from datetime import datetime, timedelta
from typing import Optional


def hash_password(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hash_password):
    return pwd_context.verify(plain_password, hash_password)


async def get_user(id: str):
    if user := await db["users"].find_one({"_id": id}):
        return user


async def authenticate_user(id, password):
    user = await db["users"].find_one({"email": id})
    if not user:
        return False
    if not verify_password(password, user["password"]):
        return False

    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = await db["users"].find_one({"email": username})
    if user is None:
        raise credentials_exception
    return user
