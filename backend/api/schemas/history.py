"""
历史记录相关的Pydantic模式
"""
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field
from uuid import UUID


class HistoryResponse(BaseModel):
    """历史记录响应"""

    id: UUID
    expression: str
    result: Optional[str]
    calculation_type: str
    created_at: datetime

    class Config:
        from_attributes = True


class HistoryListResponse(BaseModel):
    """历史记录列表响应"""

    items: List[HistoryResponse]
    total: int = Field(..., description="总记录数")
    page: int = Field(..., description="当前页码")
    page_size: int = Field(..., description="每页大小")
    total_pages: int = Field(..., description="总页数")
