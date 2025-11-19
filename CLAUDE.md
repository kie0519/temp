# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

这是一个**智能计算器全栈产品开发项目**，从产品设计到多端实现的完整实战案例。项目不仅是一个功能完善的计算器应用，更是一个展示现代软件开发全流程的标杆项目。

- **项目名称**: 智能计算器平台
- **项目类型**: 全栈产品开发实战 (产品设计 + 后端 + 前端 + AI)
- **当前版本**: v0.2.0
- **完成度**: 50% (文档、后端、Web前端已完成)
- **学习者**: kie (zuojunwei)
- **仓库地址**: https://github.com/kie0519/temp.git

## 核心架构

### 技术栈

**后端**:
- FastAPI 0.104+ (Web 框架)
- SQLAlchemy 2.0 (ORM)
- PostgreSQL/SQLite (数据库)
- JWT + bcrypt (认证加密)
- 智谱 GLM-4.6 (AI 服务)

**前端**:
- React 18 + TypeScript
- Vite (构建工具)
- Zustand (状态管理)
- Ant Design 5 (UI 组件)
- Axios (API 客户端)

### 架构模式

项目采用 **前后端分离架构**:

```
Web前端 (React)
    ↓ HTTP/JSON
FastAPI 后端 ← → 智谱 GLM AI
    ↓
PostgreSQL 数据库
```

后端采用 **分层架构**:
- `models/` - SQLAlchemy 数据库模型 (User, History, AIUsage)
- `schemas/` - Pydantic 请求/响应模式
- `services/` - 业务逻辑层 (CalculatorService, AuthService, HistoryService)
- `routers/` - API 路由层 (auth, calculate, ai, history)
- `utils/` - 工具函数 (database, security)

前端采用 **组件化架构**:
- `components/` - UI 组件 (Auth, Calculator, History, Layout)
- `stores/` - Zustand 状态管理 (useAuthStore, useCalculatorStore)
- `services/` - API 客户端封装
- `types/` - TypeScript 类型定义

## 项目结构

```
temp/
├── backend/
│   ├── api/                    # FastAPI 应用
│   │   ├── models/            # 数据库模型 (User, History, AIUsage)
│   │   ├── schemas/           # Pydantic schemas
│   │   ├── services/          # 业务逻辑层
│   │   ├── routers/           # API 路由 (10个端点)
│   │   ├── utils/             # 工具 (database, security)
│   │   ├── app.py             # 主应用入口
│   │   └── init_db.py         # 数据库初始化工具
│   ├── ai-service/            # AI 服务
│   │   └── glm_client.py      # 智谱 GLM-4.6 客户端
│   └── cli/                   # CLI 工具
│       └── calculator_cli.py  # 命令行计算器
├── frontend/
│   └── web/                   # React Web 应用
│       ├── src/
│       │   ├── components/    # UI 组件
│       │   ├── stores/        # Zustand 状态
│       │   ├── services/      # API 客户端
│       │   ├── types/         # TypeScript 类型
│       │   └── App.tsx        # 主应用
│       ├── package.json
│       └── vite.config.ts
├── docs/
│   ├── product/               # 产品文档 (BRD/MRD/PRD/FRD)
│   ├── design/                # 系统架构设计
│   ├── api/                   # API 使用指南
│   ├── DEPLOYMENT.md          # 部署指南
│   └── PROJECT_PROGRESS.md    # 进度报告
└── .env.example               # 环境变量模板
```

## 常用开发命令

### 后端开发

```bash
# 安装依赖
cd backend/api
pip install -r requirements.txt

# 初始化数据库
python init_db.py init

# 重置数据库 (开发环境)
python init_db.py reset

# 启动开发服务器
python app.py

# 或使用 uvicorn (带热重载)
uvicorn app:app --reload --host 0.0.0.0 --port 8000

# 访问 API 文档
# http://localhost:8000/docs (Swagger)
# http://localhost:8000/redoc (ReDoc)
```

### 前端开发

```bash
# 安装依赖
cd frontend/web
npm install

# 启动开发服务器
npm run dev
# 访问 http://localhost:5173

# 构建生产版本
npm run build

# 预览生产版本
npm run preview

# 类型检查
npm run lint
```

### 完整启动流程

**终端 1 - 后端**:
```bash
cd backend/api
python app.py
```

**终端 2 - 前端**:
```bash
cd frontend/web
npm run dev
```

访问 http://localhost:5173 即可使用应用

## 环境配置

### 必需的环境变量

复制 `.env.example` 到 `backend/api/.env`:

```bash
# 数据库 (默认 SQLite，可选 PostgreSQL)
DATABASE_URL=sqlite:///./calculator.db

# JWT 密钥 (生产环境务必修改!)
SECRET_KEY=your-super-secret-key-change-in-production

# 智谱 AI API Key (可选，用于 AI 计算功能)
GLM_API_KEY=your-glm-api-key-here

# CORS 允许的源
CORS_ORIGINS=http://localhost:3000,http://localhost:5173
```

### 获取 GLM API Key

访问 https://open.bigmodel.cn/ 注册并获取 API Key

## 工作规范

### Git 提交规范

- **必须使用中文进行 Git commit**
- 严格遵循 Conventional Commits 规范
- 提交格式: `<type>(<scope>): <subject>`
- 每次提交必须包含署名: `Co-Authored-By: zuojunwei`
- **不要**包含 Claude Code 相关的署名或链接

### 提交类型

- `feat`: 新功能
- `fix`: Bug 修复
- `docs`: 文档修改
- `style`: 代码格式
- `refactor`: 重构
- `test`: 测试相关
- `chore`: 其他杂项

### 提交示例

```bash
git commit -m "$(cat <<'EOF'
feat: 实现用户认证功能

本次完成内容:
- JWT token 生成和验证
- 登录和注册 API
- 密码加密 (bcrypt)

Co-Authored-By: zuojunwei
EOF
)"
```

## 核心功能模块

### 1. 认证系统 (backend/api/routers/auth.py)

**端点**:
- `POST /api/v1/auth/register` - 用户注册
- `POST /api/v1/auth/login` - 用户登录 (返回 JWT token)
- `GET /api/v1/auth/me` - 获取当前用户信息

**安全特性**:
- 密码使用 bcrypt 加密 (12 轮)
- JWT token 有效期 1 小时
- 密码强度验证 (至少 8 字符，包含大小写字母和数字)

### 2. 计算服务 (backend/api/services/calculator.py)

**核心类**: `CalculatorService`

**安全计算引擎**:
- 白名单函数: sin, cos, tan, sqrt, log, exp, abs, pow
- 防代码注入: 检测危险关键字 (`__`, `import`, `exec` 等)
- 支持常量: pi, e, tau

**API 端点**:
- `POST /api/v1/calculate` - 基础计算
- `POST /api/v1/calculate/validate` - 验证表达式
- `POST /api/v1/calculate/ai` - AI 智能计算

### 3. AI 服务 (backend/ai-service/glm_client.py)

**功能**: 将自然语言转换为数学表达式

**示例**:
- 输入: "帮我算123加456"
- 输出: 表达式 "123 + 456"，结果 579

**返回值**: `(expression: str, result: str, tokens_used: int)`

### 4. 历史记录 (backend/api/routers/history.py)

**端点**:
- `GET /api/v1/history` - 分页查询历史 (支持 page, page_size)
- `DELETE /api/v1/history/{id}` - 删除单条记录
- `DELETE /api/v1/history` - 清空所有记录
- `GET /api/v1/history/stats/ai-usage` - AI 使用统计

### 5. 前端状态管理

**useAuthStore** (stores/useAuthStore.ts):
- `login(data)` - 登录并保存 token 到 localStorage
- `register(data)` - 注册用户
- `logout()` - 登出并清除 token
- `checkAuth()` - 检查认证状态

**useCalculatorStore** (stores/useCalculatorStore.ts):
- `calculate()` - 基础计算
- `aiCalculate(query)` - AI 智能计算
- `toggleAI()` - 切换 AI 模式
- `clear()` - 清空输入和结果

## 数据库模型

### User (用户表)
```python
id: UUID (主键)
username: String(20) (唯一)
email: String(255) (唯一)
password_hash: String(255)
is_active: Boolean
is_premium: Boolean
created_at, updated_at: DateTime
```

### History (历史记录表)
```python
id: UUID (主键)
user_id: UUID (外键 → users.id)
expression: Text
result: String(255)
calculation_type: String(20)  # 'basic', 'scientific', 'ai'
created_at: DateTime
```

### AIUsage (AI 使用记录表)
```python
id: UUID (主键)
user_id: UUID (外键 → users.id)
query: Text
tokens_used: Integer
model_version: String(50)  # 默认 'glm-4.6'
created_at: DateTime
```

## API 认证流程

1. **用户登录**: POST `/api/v1/auth/login` 获取 JWT token
2. **前端保存**: token 存储在 localStorage
3. **后续请求**: Axios 拦截器自动添加 `Authorization: Bearer {token}` 头部
4. **后端验证**: `get_current_user` 依赖注入验证 token
5. **Token 过期**: 前端拦截 401 响应，自动跳转登录页

## 重要提醒

1. **所有 commit 必须使用中文**
2. **署名必须是 zuojunwei，不要包含 Claude 相关内容**
3. **修改代码后需要重启服务** (后端/前端)
4. **数据库修改后运行** `python init_db.py reset` (开发环境)
5. **前端 API 请求通过 Vite 代理** `/api` → `http://localhost:8000`
6. **推送前确认所有文件修改都已提交**

## 常见问题

### Q: ModuleNotFoundError
**解决**: `pip install -r requirements.txt`

### Q: CORS 错误
**解决**: 检查 `.env` 中的 `CORS_ORIGINS` 是否包含前端地址

### Q: AI 计算失败
**解决**: 配置 `GLM_API_KEY` 环境变量

### Q: JWT Token 过期
**解决**: 重新登录 (默认 1 小时过期)

### Q: 端口被占用
**解决**:
```bash
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# macOS/Linux
lsof -i :8000
kill -9 <PID>
```

## 文档资源

- [系统架构设计](docs/design/architecture.md) - 706 行详细架构
- [API 使用指南](docs/api/API_USAGE.md) - 完整 API 文档和示例
- [部署指南](docs/DEPLOYMENT.md) - 本地和生产环境部署
- [项目进度报告](docs/PROJECT_PROGRESS.md) - 当前完成情况
- [BRD/MRD/PRD/FRD](docs/product/) - 完整产品文档
- [Swagger 文档](http://localhost:8000/docs) - 交互式 API 文档

## Git 学习任务

项目最初是 Git 学习项目，已完成 26/26 任务 (100%)。任务清单见 [docs/development/GIT_PRACTICE_TODO.md](docs/development/GIT_PRACTICE_TODO.md)。

现已转型为全栈产品开发项目。
