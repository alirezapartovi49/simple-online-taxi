from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .respository import get_user
from ...db import get_db


router = APIRouter(prefix="/user")


@router.get("/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id=user_id)
    return user
