from datetime import datetime, timezone

from app.models.user import User


users = []
next_user_id = 1


def get_all_users():
    return users


def get_user_by_id(user_id: int):
    for user in users:
        if user.id == user_id:
            return user
        
    return None


def get_user_by_email(email: str):
    for user in users:
        if user.email == email:
            return user
        
    return None


def create_user(
    email: str,
    first_name: str, 
    last_name: str, 
    hashed_password: str, 
    date_of_birth: datetime | None = None
):
    global next_user_id

    now = datetime.now(timezone.utc)

    user = User(
        id=next_user_id,
        email=email,
        first_name=first_name,
        last_name=last_name,
        hashed_password=hashed_password,
        date_of_birth=date_of_birth,
        created_at=now,
        updated_at=now
    )

    users.append(user)
    next_user_id += 1

    print(hashed_password)

    return user