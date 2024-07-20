from pydantic import BaseModel

class QuickTask(BaseModel):
    id: int
    description: str = None

class CreateQuickTask(BaseModel):
    description: str