"""
计算路由
处理基础计算请求
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..schemas.calculate import CalculateRequest, CalculateResponse
from ..services.calculator import CalculatorService
from ..services.history import HistoryService
from ..utils.database import get_db
from ..dependencies import get_current_user
from ..models import User

router = APIRouter()


@router.post("/calculate", response_model=CalculateResponse)
def calculate(
    request: CalculateRequest,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """
    基础计算

    支持的操作:
    - 基本运算: +, -, *, /, **, %, //
    - 数学函数: sin(), cos(), tan(), sqrt(), log(), exp(), abs(), pow()
    - 数学常量: pi, e, tau

    示例:
    - `2 + 3 * 4` → 14
    - `sqrt(16)` → 4
    - `sin(pi/2)` → 1
    - `pow(2, 10)` → 1024

    需要认证: 是
    """
    try:
        # 计算结果
        result = CalculatorService.evaluate(request.expression)

        # 保存历史记录
        history = HistoryService.create_history(
            db=db,
            user_id=current_user.id,
            expression=request.expression,
            result=str(result),
            calculation_type="basic",
        )

        return CalculateResponse(
            expression=request.expression, result=result, calculation_id=history.id
        )

    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except ZeroDivisionError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"计算失败: {str(e)}"
        )


@router.post("/calculate/validate")
def validate_expression(request: CalculateRequest, current_user: User = Depends(get_current_user)):
    """
    验证表达式是否有效

    返回:
    - `valid`: 是否有效
    - `message`: 错误信息 (如果无效)

    需要认证: 是
    """
    is_valid, error_message = CalculatorService.validate_expression(request.expression)

    return {"valid": is_valid, "message": error_message if not is_valid else "表达式有效"}
