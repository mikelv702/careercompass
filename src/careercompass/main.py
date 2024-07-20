from datetime import timedelta
from typing import Annotated


from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from .auth.schemas import User, Token, UserCreate
from .auth.basic import (authenticate_user,
                         fake_users_db,
                         ACCESS_TOKEN_EXPIRE_MINUTES,
                         create_access_token,
                         get_current_active_user)
from .auth.crud import get_user_by_email, create_user, activate_user

from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from .tasks.router import router as taskrouter


app = FastAPI()
app.include_router(taskrouter)
# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db)
) -> Token:
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")




@app.post("/users/")
def register_new_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    return create_user(db=db, user=user)

@app.post("/users/activate/")
def activate_new_user(email: str, activation_code: str, db: Session = Depends(get_db)):
    activate_user(db=db, activation_code=activation_code, user_email=email)
    return {"message": "Done"}

@app.get("/users/me/", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return current_user


@app.get("/users/me/items/")
async def read_own_items(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return [{"item_id": "Foo", "owner": current_user.username}]