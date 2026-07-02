from fastapi import APIRouter, HTTPException

from app.schemas.users import UserCreate, UserResponse
from app.services.users_service import (
    register_user, 
    get_all_users, 
    get_user_by_id,
)

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post("", response_model=UserResponse)
def create_user_endpoint(user_data: UserCreate):
    user = register_user(
        email=user_data.email,
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        password=user_data.password,
        date_of_birth=user_data.date_of_birth,
    )

    if user is None:
        raise HTTPException(status_code=400, detail="Email already exists")
    
    return user


@router.get("", response_model=list[UserResponse])
def get_users():
    return get_all_users()


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    user = get_user_by_id(user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user