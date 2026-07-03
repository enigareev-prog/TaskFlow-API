from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError

from app.core.settings import (
    SECRET_KEY, 
    ALGORITHM, 
    ACCESS_TOKEN_EXPIRE_MINUTES
)


def create_access_token(data: dict):
    payload = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload.update({"exp": expire})

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM,
    )

    return token


def decode_access_token(token: str):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
        )
        return payload
    except JWTError:
        return None