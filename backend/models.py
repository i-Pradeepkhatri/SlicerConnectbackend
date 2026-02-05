from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)
    is_verified = Column(Boolean, default=False)

    # Email verification
    email_token = Column(String, nullable=True)

    # 🔐 Forgot password
    reset_token = Column(String, nullable=True)
    reset_token_expiry = Column(DateTime, nullable=True)
