from bson import ObjectId
from pydantic import BaseModel, Field, ValidationError, validator
from typing import Optional, Any
from pydantic.class_validators import Validator

from pydantic.networks import EmailStr, validate_email


class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class UserModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    first_name: str
    last_name: str
    email: EmailStr
    role : str
    is_active : bool
    is_admin : bool
    created_at: Optional[str] = None
    last_login: str
    password: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

    def __init__(__pydantic_self__,values,**data: Any) -> None:
        data = {
            "id": values.id,
            "first_name": values.first_name,
            "last_name": values.last_name,
            "email": values.email,
            "role" : values.role,
            "is_active" : values.is_active,
            "is_admin" : values.is_admin,
            "created_at": values.created_at,
            "last_login": values.last_login,
            "password": values.password,
        }
        super().__init__(**data)


class ValidateUserModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    first_name: str
    last_name: str
    email: EmailStr
    role : str
    is_active : bool
    is_admin : bool
    created_at: Optional[str] = None
    last_login: str
    password: str
    password_reverification: str
    
    @validator('first_name')
    def name_validation(cls,v):
        if ' ' in v:
            return ValidationError("No spaces should be in first_name")
        elif v is None or v == "":
            return ValidationError("first_name should be non empty")

        return v
    
    @validator('last_name')
    def last_name_validation(cls,v):
        if ' ' in v:
            return ValidationError("No spaces should be in last_name")

        return v

    @validator('password')
    def password_check(cls,v):
        if v is None:
            return ValidationError("Password field should not be empty")
        return v

    @validator('password_reverification')
    def password_match_check(cls,v, values, **kwargs):
        if 'password' in values and v!=values['password']:
            return ValidationError("Passwords do not match")
        return v

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "first_name": "John",
                "last_name": "Doe",
                "role": "simple mortal",
                "email": "abc@gmail.com",
                "is_active": False,
                "is_admin": False,
                "created_at": "datetime",
                "last_login": "datetime",
                "password": "fakehashedsecret",
                "password_reverification": "fakehashedsecret"
            }
        }


class UpdateUserModel(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    role: Optional[str]
    is_active: Optional[bool]
    is_admin: Optional[bool]
    created_at: Optional[str]
    last_login: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "first_name": "John",
                "last_name": "Doe",
                "role": "simple mortal",
                "is_active": False,
                "is_admin": False,
                "created_at": "datetime",
                "last_login": "datetime",
            }
        }


class ShowUserModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    first_name: Optional[str]
    last_name: Optional[str]
    role: Optional[str]
    is_active: Optional[bool]
    is_admin: Optional[bool]
    created_at: Optional[str]
    last_login: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "first_name": "John",
                "last_name": "Doe",
                "role": "simple mortal",
                "is_admin": False,
                "created_at": "datetime",
                "last_login": "datetime",
            }
        }
