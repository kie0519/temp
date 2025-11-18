# API 服务

## 概述
RESTful API 服务，为 Web、移动端、小程序提供计算服务。

## 技术栈
- **框架**: FastAPI
- **数据库**: SQLite (开发) / PostgreSQL (生产)
- **认证**: JWT
- **文档**: Swagger/OpenAPI

## 快速开始

### 安装依赖
```bash
cd backend/api
pip install -r requirements.txt
```

### 启动服务
```bash
# 开发模式
uvicorn app:app --reload --port 8000

# 生产模式
gunicorn app:app -w 4 -k uvicorn.workers.UvicornWorker
```

### 访问文档
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API 端点

### 计算相关
```
POST   /api/v1/calculate          # 基础计算
POST   /api/v1/calculate/advanced # 高级计算
GET    /api/v1/history            # 计算历史
DELETE /api/v1/history/:id        # 删除历史
```

### 用户相关
```
POST   /api/v1/auth/register      # 用户注册
POST   /api/v1/auth/login         # 用户登录
GET    /api/v1/user/profile       # 用户信息
PUT    /api/v1/user/profile       # 更新信息
```

### AI 相关
```
POST   /api/v1/ai/calculate       # AI 智能计算
POST   /api/v1/ai/explain         # 解题步骤
```

## 目录结构
```
api/
├── app.py              # 主应用
├── routes/             # 路由模块
│   ├── calculate.py
│   ├── user.py
│   └── ai.py
├── models/             # 数据模型
│   ├── user.py
│   └── history.py
├── services/           # 业务逻辑
│   ├── calculator.py
│   └── ai_service.py
└── utils/              # 工具函数
    ├── auth.py
    └── validators.py
```

## 环境变量
创建 `.env` 文件：
```bash
DATABASE_URL=sqlite:///./calculator.db
SECRET_KEY=your-secret-key
GLM_API_KEY=your-glm-api-key
CORS_ORIGINS=http://localhost:3000
```

## 开发计划
- [ ] 实现基础 CRUD API
- [ ] 添加用户认证系统
- [ ] 集成 AI 服务
- [ ] 添加单元测试和集成测试
- [ ] 添加 API 限流和缓存

---
**技术负责人**: zuojunwei  
**最后更新**: 2025-11-17
