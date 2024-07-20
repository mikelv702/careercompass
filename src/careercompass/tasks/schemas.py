from pydantic import BaseModel
from datetime import datetime

class QuickTask(BaseModel):
    id: int
    description: str = None
    created_at: datetime = None

class CreateQuickTask(BaseModel):
    description: str