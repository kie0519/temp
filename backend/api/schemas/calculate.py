"""
计算相关的Pydantic模式
"""
from typing import Optional
from pydantic import BaseModel, Field
from uuid import UUID


class CalculateRequest(BaseModel):
    """基础计算请求"""

    expression: str = Field(..., description="数学表达式", example="2 + 3 * 4")


class CalculateResponse(BaseModel):
    """基础计算响应"""

    expression: str = Field(..., description="原始表达式")
    result: float = Field(..., description="计算结果")
    calculation_id: UUID = Field(..., description="计算记录ID")


class AICalculateRequest(BaseModel):
    """AI计算请求"""

    query: str = Field(..., description="自然语言查询", example="帮我算123加456")


class AICalculateResponse(BaseModel):
    """AI计算响应"""

    query: str = Field(..., description="原始查询")
    understood: str = Field(..., description="AI理解的数学表达式")
    result: float = Field(..., description="计算结果")
    calculation_id: UUID = Field(..., description="计算记录ID")
    tokens_used: Optional[int] = Field(None, description="使用的token数量")
