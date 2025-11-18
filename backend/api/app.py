"""
智能计算器 API 服务
FastAPI 主应用入口
"""
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from utils.database import init_db

# 加载环境变量
load_dotenv()

app = FastAPI(
    title="智能计算器 API",
    description="提供计算服务、用户管理和 AI 增强功能",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS 配置 - 从环境变量读取允许的源
CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    """应用启动时初始化数据库"""
    print("🚀 正在启动应用...")
    init_db()
    print("✅ 应用启动完成")

@app.get("/")
async def root():
    """根路径"""
    return {
        "message": "欢迎使用智能计算器 API",
        "version": "0.1.0",
        "docs": "/docs"
    }

@app.get("/health")
async def health_check():
    """健康检查"""
    return {"status": "healthy"}

# TODO: 引入路由模块
# from routes import calculate, user, ai
# app.include_router(calculate.router, prefix="/api/v1", tags=["计算"])
# app.include_router(user.router, prefix="/api/v1", tags=["用户"])
# app.include_router(ai.router, prefix="/api/v1", tags=["AI"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
