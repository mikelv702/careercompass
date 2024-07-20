from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")


class QuickTasks(Base):
    __tablename__="quicktasks"

    id = Column(Integer, primary_key=True)
    description = Column(String)
    created_at = Column(DateTime, server_default=func.now())
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="quicktasks")