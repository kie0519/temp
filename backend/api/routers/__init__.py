"""
API 路由模块
"""
from .auth import router as auth_router
from .calculate import router as calculate_router
from .history import router as history_router
from .ai import router as ai_router

__all__ = ["auth_router", "calculate_router", "history_router", "ai_router"]
