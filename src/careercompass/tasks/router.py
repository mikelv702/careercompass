from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..auth.basic import get_current_active_user
from ..auth.schemas import User
from typing import Annotated
from .crud import get_quicktask_for_user, create_quicktask
from ..database import SessionLocal


router = APIRouter(prefix='/quicktask', tags=['task'])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get('/')
def read_tasks(current_user: Annotated[User, Depends(get_current_active_user)],
               db: Session = Depends(get_db)):

    return get_quicktask_for_user(db=db, user_id=current_user.id)

@router.post('/')
def create_task(description:str, current_user: Annotated[User, Depends(get_current_active_user)],
               db: Session = Depends(get_db)):
    created_task = create_quicktask(db, description, current_user.id)
    return created_task