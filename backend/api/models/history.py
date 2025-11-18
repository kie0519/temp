"""
历史记录和AI使用记录模型
"""
from datetime import datetime
from sqlalchemy import Column, String, Integer, Text, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from ..utils.database import Base


class History(Base):
    """计算历史记录模型"""

    __tablename__ = "history"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    expression = Column(Text, nullable=False)
    result = Column(String(255), nullable=True)
    calculation_type = Column(String(20), default="basic", nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False, index=True)

    # 关系
    user = relationship("User", back_populates="history_records")

    def __repr__(self):
        return f"<History(id={self.id}, user_id={self.user_id}, expression={self.expression[:20]}...)>"


class AIUsage(Base):
    """AI使用记录模型"""

    __tablename__ = "ai_usage"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    query = Column(Text, nullable=False)
    tokens_used = Column(Integer, nullable=False)
    model_version = Column(String(50), default="glm-4.6", nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False, index=True)

    # 关系
    user = relationship("User", back_populates="ai_usage_records")

    def __repr__(self):
        return f"<AIUsage(id={self.id}, user_id={self.user_id}, tokens={self.tokens_used})>"
