from datetime import date, datetime
from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy import select
from app.core.utils import hash_password
from app.core.database import get_db
from .models import User
from .schemas import UserCreate, UserResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.logger import logging

router = APIRouter()

logger = logging.getLogger(__name__)


@router.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    db_user = User(**user.model_dump())
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    logger.info("User created: %s", db_user.id) 
    return db_user


@router.get("/get_users", response_model=List[UserResponse])
async def get_users(db: AsyncSession = Depends(get_db)):
    logger.info("Getting all users")
    query = select(User).where(User.is_active == 1)
    users = await db.execute(query)
    return users.scalars().all()


@router.get("/get_user/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    logger.info("Getting user with id: %s", user_id)
    query = select(User).where(User.id == user_id, User.is_active == 1)
    user = await db.execute(query)
    user = user.scalars().first()
    if user is None:
        logger.warning("User with id %s not found", user_id)
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/update_user/{user_id}", response_model=UserResponse)
async def update_user(
    user_id: int, user: dict, db: AsyncSession = Depends(get_db)
):
    logger.info("Updating user with id: %s", user_id)
    query = select(User).where(User.id == user_id, User.is_active == 1)
    db_user = await db.execute(query)
    db_user = db_user.scalars().first()
    if db_user is None:
        logger.warning("User with id %s not found", user_id)
        raise HTTPException(status_code=404, detail="User not found")
    for key, value in user.items():
        if key == "password":
            value = hash_password(value)
        if key == "date_of_birth":
            value = date.fromisoformat(value)
        setattr(db_user, key, value)
    await db.commit()
    await db.refresh(db_user)
    return db_user


@router.delete("/delete_user/{user_id}")
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    logger.info("Deleting user with id: %s", user_id)
    query = select(User).where(User.id == user_id)
    db_user = await db.execute(query)
    db_user = db_user.scalars().first()
    if db_user is None:
        logger.warning("User with id %s not found", user_id)
        raise HTTPException(status_code=404, detail="User not found")
    db_user.is_active = 0
    await db.commit()
    return {"message": "User deleted successfully"}
