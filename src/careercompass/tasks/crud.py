from datetime import datetime

from ..models import QuickTasks
from sqlalchemy.orm import Session
from .schemas import CreateQuickTask


def create_quicktask(db: Session, description: CreateQuickTask, user_id: int):
    db_quicktask = QuickTasks(description=description.description, user_id=user_id)
    db.add(db_quicktask)
    db.commit()
    db.refresh(db_quicktask)
    return db_quicktask


def get_quicktask_for_user(db: Session, user_id: int,
                           skip: int = 0, limit: int = 100):
    return db.query(QuickTasks).filter(QuickTasks.user_id == user_id).offset(skip).limit(limit).all()


def get_quicktask_for_user_query(db: Session, user_id: int,
                                 skip: int = 0, limit: int = 100,
                                 from_date: datetime = None, to_date: datetime = None, ):
    query_filter = db.query(QuickTasks).filter(QuickTasks.user_id == user_id)
    if from_date:
        print(f'from: {from_date}')
        query_filter = query_filter.filter(QuickTasks.created_at >= from_date)
    if to_date:
        print(f'to: {to_date}')
        query_filter = query_filter.filter(QuickTasks.created_at <= to_date)
    return query_filter.offset(skip).limit(limit).all()
