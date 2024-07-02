from typing import Optional
from pydantic import BaseModel, Field, field_validator
from datetime import datetime, date
import re
from app.core.utils import hash_password, verify_password


class UserCreate(BaseModel):
    company_name: str = Field(example="ABC Inc.")
    first_name: str = Field(example="John")
    last_name: str = Field(example="Doe")
    email: str = Field(example="email@email.com")
    password: str = Field(example="Test@123")
    mobile: str = Field(example="1234567890")
    hashtag: str = Field(example="#hashtag")
    date_of_birth: date = Field(example="2021-01-01")

    @field_validator("password")
    def password_must_be_valid(cls, password):
        if password and not re.match(
            r"^(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*])(?=.{8,})", password
        ):
            raise ValueError(
                "Password must have atleast 8 characters and 1 special character and 1 number and 1 uppercase letter"
            )
        if password:
            password = hash_password(password)
        return password

    @field_validator("email")
    def email_must_be_valid(cls, email):
        if email and not re.match(
            r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", email
        ):
            raise ValueError("Invalid email")
        return email



class UserResponse(BaseModel):
    id: Optional[int]
    company_name: Optional[str]
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    mobile: Optional[str]
    hashtag: Optional[str]
    date_of_birth: Optional[date]
    is_active: Optional[int]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
