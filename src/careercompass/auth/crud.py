from sqlalchemy.orm import Session
from . import models, schemas
from passlib.context import CryptContext


def get_password_hash(password):
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    return pwd_context.hash(password)


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_user_by_email(db: Session, email: str):
    print("get user")
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    print("CREATING USER")
    fake_hashed_password = get_password_hash(user.password)
    print(fake_hashed_password)
    db_user = models.User(email=user.email,
                          hashed_password=fake_hashed_password,
                          username=user.username,
                          full_name=user.full_name,
                          )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    print(db_user)
    return db_user.username


def activate_user(db: Session, user_email: str, activation_code: str):
    user = db.query(models.User).filter(models.User.email == user_email).first()
    test_code = "signup123"
    if activation_code == test_code:
        user.is_active = True
        db.commit()
        db.refresh(user)
        if user.is_active:
            print(f"{user.email} is now active")
        else:
            print(f"Unable to activate {user.email}")