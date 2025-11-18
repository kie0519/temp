"""
AI 计算路由
处理AI增强的计算请求
"""
import sys
import os

# 添加 ai-service 到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../../ai-service"))

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..schemas.calculate import AICalculateRequest, AICalculateResponse
from ..services.calculator import CalculatorService
from ..services.history import HistoryService
from ..utils.database import get_db
from ..dependencies import get_current_user
from ..models import User

try:
    from glm_client import GLMClient
except ImportError:
    GLMClient = None

router = APIRouter()


@router.post("/calculate/ai", response_model=AICalculateResponse)
def ai_calculate(
    request: AICalculateRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    AI 智能计算

    使用自然语言描述计算需求, AI会理解并执行计算

    示例:
    - "帮我算123加456"
    - "计算100的平方根"
    - "sin30度是多少"
    - "2的10次方"

    流程:
    1. AI 理解自然语言请求
    2. 提取标准数学表达式
    3. 执行计算
    4. 保存历史记录和AI使用记录

    需要认证: 是
    需要配置: GLM_API_KEY 环境变量
    """
    # 检查 GLM 客户端是否可用
    if GLMClient is None:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="AI服务暂不可用, 请联系管理员配置GLM_API_KEY",
        )

    try:
        # 初始化 GLM 客户端
        glm_client = GLMClient()

        # 使用 AI 理解请求
        expression, ai_result, tokens_used = glm_client.calculate(request.query)

        # 使用计算器服务验证和计算
        try:
            result = CalculatorService.evaluate(expression)
        except Exception:
            # 如果表达式无效, 使用 AI 的结果
            try:
                result = float(ai_result)
            except ValueError:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"AI无法理解计算请求: {request.query}",
                )

        # 保存历史记录
        history = HistoryService.create_history(
            db=db,
            user_id=current_user.id,
            expression=expression,
            result=str(result),
            calculation_type="ai",
        )

        # 保存 AI 使用记录
        HistoryService.create_ai_usage(
            db=db, user_id=current_user.id, query=request.query, tokens_used=tokens_used
        )

        return AICalculateResponse(
            query=request.query,
            understood=expression,
            result=result,
            calculation_id=history.id,
            tokens_used=tokens_used,
        )

    except ValueError as e:
        if "GLM_API_KEY" in str(e):
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="AI服务未配置, 请联系管理员",
            )
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"AI计算失败: {str(e)}"
        )
