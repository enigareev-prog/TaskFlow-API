import bcrypt


from app.repositories.users_repository import (
    create_user,
    get_all_users,
    get_user_by_id,
    get_user_by_email,
)
from app.core.security import create_access_token


def hash_password(password: str) -> str:
    password_bytes = password.encode('utf-8')

    hashed = bcrypt.hashpw(
        password_bytes,
        bcrypt.gensalt()
    )

    return hashed.decode("utf-8")


def register_user(
    email: str,
    first_name: str,
    last_name: str,
    password: str,
    date_of_birth,
): 
    existing_user = get_user_by_email(email)

    if existing_user is not None:
        return None
    
    hashed_password = hash_password(password)

    return create_user(
        email=email,
        first_name=first_name,
        last_name=last_name,
        hashed_password=hashed_password,
        date_of_birth=date_of_birth,
    )


def check_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(
        password.encode("utf-8"),
        hashed_password.encode("utf-8")
    )


def login_user(email: str, password: str):
    user = get_user_by_email(email)

    if user is None:
        return None
    
    if not check_password(password, user.hashed_password):
        return None
    
    access_token = create_access_token(
        data={"user_id": user.id}
    )
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
    }