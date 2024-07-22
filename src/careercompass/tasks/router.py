from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..auth.basic import get_current_active_user
from ..auth.schemas import User
from typing import Annotated
from .crud import get_quicktask_for_user, create_quicktask, get_quicktask_for_user_query
from ..database import SessionLocal
from .schemas import CreateQuickTask
from ..depends import get_db


router = APIRouter(prefix='/quicktask', tags=['task'])


@router.get('/')
def read_tasks(current_user: Annotated[User, Depends(get_current_active_user)],
               skip: int = 0, limit: int = 10,
               db: Session = Depends(get_db)):
    return get_quicktask_for_user(db=db, user_id=current_user.id,
                                  skip=skip,
                                  limit = limit)


@router.get('/query')
def get_tasks_query(current_user: Annotated[User, Depends(get_current_active_user)],
               skip: int = 0, limit: int = 100,
                from_date: datetime = None, to_date:datetime = None,
               db: Session = Depends(get_db)):
    return get_quicktask_for_user_query(db=db, user_id=current_user.id, skip=skip,
                                        limit=limit, from_date=from_date, to_date=to_date)


@router.post('/')
def create_task(description:CreateQuickTask, current_user: Annotated[User, Depends(get_current_active_user)],
               db: Session = Depends(get_db)):
    created_task = create_quicktask(db, description, current_user.id)
    return created_task