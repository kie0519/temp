"""
安全工具模块
处理密码哈希、JWT生成和验证
"""
import os
from datetime import datetime, timedelta
from typing import Optional
from passlib.context import CryptContext
from jose import JWTError, jwt

# 密码加密上下文 (bcrypt, 12轮)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT配置
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # 1小时


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    验证密码

    Args:
        plain_password: 明文密码
        hashed_password: 哈希后的密码

    Returns:
        bool: 密码是否匹配
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    生成密码哈希

    Args:
        password: 明文密码

    Returns:
        str: 哈希后的密码
    """
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """
    创建JWT访问令牌

    Args:
        data: 要编码的数据 (通常包含user_id, username等)
        expires_delta: 过期时间间隔

    Returns:
        str: JWT令牌
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str) -> Optional[dict]:
    """
    解码JWT访问令牌

    Args:
        token: JWT令牌

    Returns:
        Optional[dict]: 解码后的数据,如果无效则返回None
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None


def validate_password_strength(password: str) -> tuple[bool, str]:
    """
    验证密码强度

    要求:
    - 至少8个字符
    - 包含大写字母
    - 包含小写字母
    - 包含数字

    Args:
        password: 密码

    Returns:
        tuple[bool, str]: (是否有效, 错误信息)
    """
    if len(password) < 8:
        return False, "密码长度至少为8个字符"

    if not any(c.isupper() for c in password):
        return False, "密码必须包含至少一个大写字母"

    if not any(c.islower() for c in password):
        return False, "密码必须包含至少一个小写字母"

    if not any(c.isdigit() for c in password):
        return False, "密码必须包含至少一个数字"

    return True, ""
