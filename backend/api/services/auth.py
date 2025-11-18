"""
认证服务
处理用户注册、登录和令牌管理
"""
from datetime import timedelta
from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from ..models import User
from ..schemas.auth import UserCreate, UserLogin, Token, UserResponse
from ..utils.security import (
    verify_password,
    get_password_hash,
    create_access_token,
    validate_password_strength,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)


class AuthService:
    """认证服务类"""

    @staticmethod
    def register_user(db: Session, user_data: UserCreate) -> UserResponse:
        """
        注册新用户

        Args:
            db: 数据库会话
            user_data: 用户注册数据

        Returns:
            UserResponse: 用户信息

        Raises:
            HTTPException: 用户名或邮箱已存在
        """
        # 检查用户名是否已存在
        if db.query(User).filter(User.username == user_data.username).first():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="用户名已被使用"
            )

        # 检查邮箱是否已存在
        if db.query(User).filter(User.email == user_data.email).first():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="邮箱已被注册"
            )

        # 验证密码强度
        is_valid, error_message = validate_password_strength(user_data.password)
        if not is_valid:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=error_message)

        # 创建用户
        hashed_password = get_password_hash(user_data.password)
        db_user = User(
            username=user_data.username, email=user_data.email, password_hash=hashed_password
        )

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return UserResponse.from_orm(db_user)

    @staticmethod
    def login_user(db: Session, login_data: UserLogin) -> Token:
        """
        用户登录

        Args:
            db: 数据库会话
            login_data: 登录数据

        Returns:
            Token: JWT令牌和用户信息

        Raises:
            HTTPException: 邮箱或密码错误
        """
        # 查找用户
        user = db.query(User).filter(User.email == login_data.email).first()

        # 验证用户和密码
        if not user or not verify_password(login_data.password, user.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="邮箱或密码错误",
                headers={"WWW-Authenticate": "Bearer"},
            )

        # 检查用户是否激活
        if not user.is_active:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="账户已被禁用")

        # 创建访问令牌
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": str(user.id), "username": user.username}, expires_delta=access_token_expires
        )

        return Token(
            access_token=access_token,
            token_type="bearer",
            expires_in=ACCESS_TOKEN_EXPIRE_MINUTES * 60,
            user=UserResponse.from_orm(user),
        )

    @staticmethod
    def get_current_user(db: Session, user_id: str) -> User:
        """
        获取当前用户

        Args:
            db: 数据库会话
            user_id: 用户ID

        Returns:
            User: 用户对象

        Raises:
            HTTPException: 用户不存在
        """
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="用户不存在")

        return user
