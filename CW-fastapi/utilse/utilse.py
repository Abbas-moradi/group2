from hashlib import sha256
from storeage.storage import collection_user
from fastapi import HTTPException, status
from datetime import datetime, timedelta
from hashlib import sha256
from jose import jwt
import re


def hash_password(password: str) -> str:
    return sha256(password.encode()).hexdigest()


def verify_password(password: str, hashed_password: str) -> bool:
    return hash_password(password) == hashed_password


def email_validation(email: str) -> str:
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if not re.search(regex, email):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Email format is not correct"
            )
    if list(collection_user.find({"email": email})):
        return True
    return False


def encode_access_token(data: dict):
    secret_key = "SECRET-KEY"
    algorithm = "HS256"
    expire = datetime.utcnow() + timedelta(minutes=30)
    data.update({"expire_date": datetime.strftime(expire, "%Y %m %d")})
    encoded_token = jwt.encode(data, str(secret_key), algorithm=algorithm)
    return encoded_token


def decode_access_token(token: str):
    secret_key = "SECRET-KEY"
    algorithm = ["HS256"]
    decoded_token = jwt.decode(token, str(secret_key), algorithms=algorithm)
    return decoded_token
