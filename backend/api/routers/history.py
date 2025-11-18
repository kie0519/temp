"""
历史记录路由
处理历史记录查询和管理
"""
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from uuid import UUID

from ..schemas.history import HistoryListResponse
from ..services.history import HistoryService
from ..utils.database import get_db
from ..dependencies import get_current_user
from ..models import User

router = APIRouter()


@router.get("/history", response_model=HistoryListResponse)
def get_history(
    page: int = Query(1, ge=1, description="页码"),
    page_size: int = Query(20, ge=1, le=100, description="每页大小"),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    获取当前用户的计算历史记录

    支持分页查询:
    - **page**: 页码 (从1开始)
    - **page_size**: 每页大小 (1-100)

    返回:
    - **items**: 历史记录列表
    - **total**: 总记录数
    - **page**: 当前页码
    - **page_size**: 每页大小
    - **total_pages**: 总页数

    需要认证: 是
    """
    return HistoryService.get_user_history(db, current_user.id, page, page_size)


@router.delete("/history/{history_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_history(
    history_id: UUID,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    删除指定的历史记录

    - **history_id**: 历史记录ID

    需要认证: 是
    """
    success = HistoryService.delete_history(db, current_user.id, history_id)

    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="历史记录不存在")

    return None


@router.delete("/history", status_code=status.HTTP_200_OK)
def clear_history(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """
    清空当前用户的所有历史记录

    返回删除的记录数

    需要认证: 是
    """
    count = HistoryService.clear_user_history(db, current_user.id)

    return {"message": "历史记录已清空", "deleted_count": count}


@router.get("/history/stats/ai-usage")
def get_ai_usage_stats(
    current_user: User = Depends(get_current_user), db: Session = Depends(get_db)
):
    """
    获取当前用户的AI使用统计

    返回:
    - **total_queries**: 总查询次数
    - **total_tokens**: 总使用token数

    需要认证: 是
    """
    stats = HistoryService.get_user_ai_usage_stats(db, current_user.id)
    return stats
