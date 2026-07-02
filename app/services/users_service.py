from app.repositories.users_repository import (
    create_user,
    get_all_users,
    get_user_by_id,
    get_user_by_email,
)


def hash_password(password: str):
    return f"hashed_{password}"


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