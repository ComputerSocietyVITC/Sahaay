from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from settings import (pwd_context,)
#db, 
#                       oauth2_scheme,
#                       SECRET_KEY, ALGORITHM)

from datetime import datetime, timedelta
from typing import Optional

def hash_password(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hash_password):
    return pwd_context.verify(plain_password,hash_password)