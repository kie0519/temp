"""
认证相关的Pydantic模式
"""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from uuid import UUID


class UserCreate(BaseModel):
    """用户注册请求"""

    username: str = Field(..., min_length=3, max_length=20, description="用户名")
    email: EmailStr = Field(..., description="邮箱地址")
    password: str = Field(..., min_length=8, description="密码")


class UserLogin(BaseModel):
    """用户登录请求"""

    email: EmailStr = Field(..., description="邮箱地址")
    password: str = Field(..., description="密码")


class UserResponse(BaseModel):
    """用户信息响应"""

    id: UUID
    username: str
    email: str
    is_active: bool
    is_premium: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True  # SQLAlchemy 2.0 兼容


class Token(BaseModel):
    """JWT令牌响应"""

    access_token: str
    token_type: str = "bearer"
    expires_in: int = 3600  # 秒
    user: Optional[UserResponse] = None
