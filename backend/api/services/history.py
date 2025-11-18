"""
历史记录服务
处理计算历史和AI使用记录
"""
import math
from uuid import UUID
from sqlalchemy.orm import Session
from sqlalchemy import func

from ..models import History, AIUsage, User
from ..schemas.history import HistoryResponse, HistoryListResponse


class HistoryService:
    """历史记录服务类"""

    @staticmethod
    def create_history(
        db: Session, user_id: UUID, expression: str, result: str, calculation_type: str = "basic"
    ) -> History:
        """
        创建历史记录

        Args:
            db: 数据库会话
            user_id: 用户ID
            expression: 表达式
            result: 计算结果
            calculation_type: 计算类型 (basic/scientific/ai)

        Returns:
            History: 历史记录对象
        """
        history = History(
            user_id=user_id, expression=expression, result=result, calculation_type=calculation_type
        )

        db.add(history)
        db.commit()
        db.refresh(history)

        return history

    @staticmethod
    def get_user_history(
        db: Session, user_id: UUID, page: int = 1, page_size: int = 20
    ) -> HistoryListResponse:
        """
        获取用户历史记录

        Args:
            db: 数据库会话
            user_id: 用户ID
            page: 页码 (从1开始)
            page_size: 每页大小

        Returns:
            HistoryListResponse: 历史记录列表
        """
        # 查询总数
        total = db.query(func.count(History.id)).filter(History.user_id == user_id).scalar()

        # 查询分页数据
        records = (
            db.query(History)
            .filter(History.user_id == user_id)
            .order_by(History.created_at.desc())
            .offset((page - 1) * page_size)
            .limit(page_size)
            .all()
        )

        # 转换为响应模型
        items = [HistoryResponse.from_orm(record) for record in records]

        # 计算总页数
        total_pages = math.ceil(total / page_size) if total > 0 else 0

        return HistoryListResponse(
            items=items, total=total, page=page, page_size=page_size, total_pages=total_pages
        )

    @staticmethod
    def delete_history(db: Session, user_id: UUID, history_id: UUID) -> bool:
        """
        删除历史记录

        Args:
            db: 数据库会话
            user_id: 用户ID
            history_id: 历史记录ID

        Returns:
            bool: 是否删除成功
        """
        record = (
            db.query(History).filter(History.id == history_id, History.user_id == user_id).first()
        )

        if record:
            db.delete(record)
            db.commit()
            return True

        return False

    @staticmethod
    def clear_user_history(db: Session, user_id: UUID) -> int:
        """
        清空用户历史记录

        Args:
            db: 数据库会话
            user_id: 用户ID

        Returns:
            int: 删除的记录数
        """
        count = db.query(History).filter(History.user_id == user_id).delete()
        db.commit()
        return count

    @staticmethod
    def create_ai_usage(db: Session, user_id: UUID, query: str, tokens_used: int) -> AIUsage:
        """
        创建AI使用记录

        Args:
            db: 数据库会话
            user_id: 用户ID
            query: 查询内容
            tokens_used: 使用的token数

        Returns:
            AIUsage: AI使用记录对象
        """
        ai_usage = AIUsage(user_id=user_id, query=query, tokens_used=tokens_used)

        db.add(ai_usage)
        db.commit()
        db.refresh(ai_usage)

        return ai_usage

    @staticmethod
    def get_user_ai_usage_stats(db: Session, user_id: UUID) -> dict:
        """
        获取用户AI使用统计

        Args:
            db: 数据库会话
            user_id: 用户ID

        Returns:
            dict: 统计信息
        """
        total_queries = db.query(func.count(AIUsage.id)).filter(AIUsage.user_id == user_id).scalar()

        total_tokens = (
            db.query(func.sum(AIUsage.tokens_used)).filter(AIUsage.user_id == user_id).scalar() or 0
        )

        return {"total_queries": total_queries, "total_tokens": total_tokens}
