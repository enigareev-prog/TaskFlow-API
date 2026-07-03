from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.core.security import decode_access_token
from app.repositories.users_repository import get_user_by_id

security = HTTPBearer()


def get_current_user(
        credentials: HTTPAuthorizationCredentials = Depends(security),
): 
    token = credentials.credentials
    payload = decode_access_token(token)

    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    user_id = payload.get("user_id")

    if user_id is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    user = get_user_by_id(user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user