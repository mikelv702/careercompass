from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base
from ..models import Item, QuickTasks

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=False)
    full_name = Column(String)

    items = relationship("Item", back_populates="owner")
    quicktasks = relationship("QuickTasks", back_populates="user")

