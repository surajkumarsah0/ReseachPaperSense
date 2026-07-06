# app/models/user.py
import uuid
from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID # PostgreSQL native UUID support tanyau
from app.database.session import Base


class User(Base):
    __tablename__ = "users"

    # 🔑 AUTO-UUID GENERATOR CONFIGURATION
    # default=uuid.uuid4 le naya record thapida random 36-character id auto-assign garcha
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=True) # Password column
    auth_provider = Column(String, default="local", nullable=False) # authprovider