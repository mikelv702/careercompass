from pydantic import BaseModel



# Quick Task Schemas

class QuickTaskBase(BaseModel):
    description: str | None = None
    
class QuickTaskCreate(QuickTaskBase):
    pass

class QuickTask(QuickTaskBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

# User Schemas

class UserBase(BaseModel):
    email: str
    
class UserCreate(UserBase):
    password: str
    
class User(UserBase):
    id: int
    is_active: bool
    quick_tasks: list[QuickTask] = []
    
    class Config:
        orm_mode = True