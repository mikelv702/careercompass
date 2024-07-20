from ..models import QuickTasks
from sqlalchemy.orm import Session


def create_quicktask(db: Session, description:str):
    db_quicktask = QuickTasks(description=description)
    db.add(db_quicktask)
    db.commit()
    db.refresh(db_quicktask)
    return db_quicktask


def get_quicktask_for_user(db: Session, user_id: int,
                   skip: int = 0, limit: int = 100):
    return db.query(QuickTasks).filter(QuickTasks.user.user_id == user_id).offset(skip).limit(limit).all()