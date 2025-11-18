"""
数据库工具模块
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 从环境变量获取数据库URL,默认使用SQLite
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./calculator.db")

# 创建数据库引擎
# SQLite需要特殊配置
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(DATABASE_URL, connect_args=connect_args)

# 创建会话工厂
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 创建基类
Base = declarative_base()


def get_db():
    """
    获取数据库会话的依赖注入函数
    用于FastAPI的Depends
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """
    初始化数据库
    创建所有表
    """
    # 导入所有模型以确保它们被注册
    from ..models import User, History, AIUsage

    # 创建所有表
    Base.metadata.create_all(bind=engine)
    print("✅ 数据库表已创建")


def drop_db():
    """
    删除所有表(仅用于开发/测试)
    """
    Base.metadata.drop_all(bind=engine)
    print("⚠️  数据库表已删除")
