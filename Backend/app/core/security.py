# app/core/security.py
import os
from datetime import datetime, timedelta, timezone
import jwt
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = "HS256"

# Expiry windows configuration settings
ACCESS_TOKEN_EXPIRE_MINUTES = 15  # Short-lived (Security guard)
REFRESH_TOKEN_EXPIRE_DAYS = 7     # Long-lived (Key to generate new tokens)

def create_access_token(data: dict) -> str:
    # """Short-lived signature encoder (Access Token)"""
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire, "token_type": "access"})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def create_refresh_token(data: dict) -> str:
    # """Long-lived signature encoder (Refresh Token)"""
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire, "token_type": "refresh"})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)