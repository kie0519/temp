"""
认证路由
处理用户注册和登录
"""
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from ..schemas.auth import UserCreate, UserLogin, Token, UserResponse
from ..services.auth import AuthService
from ..utils.database import get_db
from ..dependencies import get_current_user
from ..models import User

router = APIRouter()


@router.post("/auth/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    """
    用户注册

    - **username**: 用户名 (3-20字符)
    - **email**: 邮箱地址
    - **password**: 密码 (至少8字符, 包含大小写字母和数字)
    """
    return AuthService.register_user(db, user_data)


@router.post("/auth/login", response_model=Token)
def login(login_data: UserLogin, db: Session = Depends(get_db)):
    """
    用户登录

    - **email**: 邮箱地址
    - **password**: 密码

    返回JWT访问令牌, 有效期1小时
    """
    return AuthService.login_user(db, login_data)


@router.get("/auth/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)):
    """
    获取当前用户信息

    需要在请求头中携带有效的JWT令牌:
    ```
    Authorization: Bearer {token}
    ```
    """
    return UserResponse.from_orm(current_user)
