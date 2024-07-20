from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class UserBase(BaseModel):
    email: str | None = None
    full_name: str | None = None


class User(UserBase):
    username: str
    is_active: bool | None = None

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    username: str
    password: str


class UserInDB(User):
    hashed_password: str
