# 系统架构设计文档

## 文档信息

- **项目名称**: 智能计算器平台
- **文档版本**: v1.0
- **创建日期**: 2025-11-17
- **最后更新**: 2025-11-18
- **作者**: zuojunwei

## 1. 架构概览

### 1.1 整体架构

```
┌─────────────────────────────────────────────────────────────┐
│                         客户端层                             │
│  Web浏览器  │  桌面应用  │  移动APP  │  小程序  │  硬件设备   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      API网关层 (未来)                        │
│           负载均衡 │ 限流 │ 认证 │ 日志 │ 监控                │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                       应用服务层                             │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  计算服务     │  │  用户服务     │  │  AI服务      │      │
│  │  FastAPI     │  │  FastAPI     │  │  GLM-4.6     │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│                                                              │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                        数据层                                │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  PostgreSQL  │  │  Redis缓存   │  │  对象存储     │      │
│  │  主数据库     │  │  会话/结果   │  │  日志/备份    │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 1.2 技术栈选型

#### 后端技术栈
- **Web框架**: FastAPI 0.104+
  - 理由: 高性能、异步支持、自动API文档、类型提示
- **数据库**: PostgreSQL 14+
  - 理由: 开源、成熟、JSON支持、强大的事务处理
- **缓存**: Redis 7+
  - 理由: 高性能、支持多种数据结构、持久化
- **ORM**: SQLAlchemy 2.0+
  - 理由: 功能强大、支持异步、类型安全
- **认证**: JWT (PyJWT)
  - 理由: 无状态、易于扩展、标准化

#### 前端技术栈
- **Web**: React 18 + TypeScript + Vite
  - 理由: 生态丰富、性能优秀、开发体验好
- **状态管理**: Zustand
  - 理由: 简单、轻量、TypeScript友好
- **UI组件**: Ant Design 5
  - 理由: 企业级、组件丰富、中文文档完善
- **HTTP客户端**: Axios
  - 理由: 功能完善、拦截器支持、易于封装

#### AI集成
- **模型**: 智谱 GLM-4.6
  - 理由: 中文优化、数学能力强、API稳定

#### DevOps
- **容器化**: Docker + Docker Compose
- **编排**: Kubernetes (生产环境)
- **CI/CD**: GitHub Actions
- **监控**: Prometheus + Grafana
- **日志**: ELK Stack

## 2. 模块设计

### 2.1 后端模块结构

```
backend/
├── cli/                    # CLI模块
│   ├── calculator_cli.py   # 命令行计算器
│   └── constants.py        # 数学常量
│
├── api/                    # API模块
│   ├── app.py             # FastAPI主应用
│   ├── routers/           # 路由模块
│   │   ├── calculate.py   # 计算相关路由
│   │   ├── auth.py        # 认证相关路由
│   │   └── history.py     # 历史记录路由
│   ├── models/            # 数据模型
│   │   ├── user.py        # 用户模型
│   │   └── history.py     # 历史记录模型
│   ├── schemas/           # Pydantic模式
│   │   ├── calculate.py   # 计算请求/响应模式
│   │   ├── auth.py        # 认证模式
│   │   └── history.py     # 历史记录模式
│   ├── services/          # 业务逻辑
│   │   ├── calculator.py  # 计算服务
│   │   ├── auth.py        # 认证服务
│   │   └── history.py     # 历史服务
│   └── utils/             # 工具函数
│       ├── security.py    # 安全工具
│       └── database.py    # 数据库工具
│
└── ai-service/            # AI服务模块
    ├── glm_client.py      # GLM客户端
    └── prompts/           # 提示词模板
```

### 2.2 前端模块结构

```
frontend/
└── web/
    ├── src/
    │   ├── components/       # UI组件
    │   │   ├── Calculator/   # 计算器组件
    │   │   ├── History/      # 历史记录组件
    │   │   └── Auth/         # 认证组件
    │   ├── stores/           # 状态管理
    │   │   ├── useAuthStore.ts
    │   │   └── useCalculatorStore.ts
    │   ├── services/         # API服务
    │   │   ├── api.ts        # API封装
    │   │   └── auth.ts       # 认证服务
    │   ├── hooks/            # 自定义Hooks
    │   ├── utils/            # 工具函数
    │   └── types/            # TypeScript类型
    └── public/               # 静态资源
```

## 3. 数据流设计

### 3.1 用户登录流程

```
┌──────┐    1.输入凭证     ┌──────────┐
│ 用户 │ ──────────────→  │  前端    │
└──────┘                   └──────────┘
                                │
                                │ 2.POST /auth/login
                                ▼
                           ┌──────────┐
                           │ API服务  │
                           └──────────┘
                                │
                                │ 3.验证密码
                                ▼
                           ┌──────────┐
                           │ 数据库   │
                           └──────────┘
                                │
                                │ 4.返回用户信息
                                ▼
                           ┌──────────┐
                           │ API服务  │
                           └──────────┘
                                │
                                │ 5.生成JWT
                                │ 6.返回token
                                ▼
                           ┌──────────┐
                           │  前端    │
                           └──────────┘
                                │
                                │ 7.存储token
                                ▼
                           ┌──────────┐
                           │LocalStorage│
                           └──────────┘
```

### 3.2 基础计算流程

```
┌──────┐    1.输入表达式   ┌──────────┐
│ 用户 │ ──────────────→  │  前端    │
└──────┘                   └──────────┘
                                │
                                │ 2.POST /calculate
                                │   + JWT token
                                ▼
                           ┌──────────┐
                           │ API服务  │
                           └──────────┘
                                │
                                │ 3.验证token
                                ▼
                           ┌──────────┐
                           │认证中间件 │
                           └──────────┘
                                │
                                │ 4.执行计算
                                ▼
                           ┌──────────┐
                           │计算引擎  │
                           └──────────┘
                                │
                    ┌───────────┴───────────┐
                    │                       │
              5a.保存历史              5b.缓存结果
                    ▼                       ▼
               ┌──────────┐          ┌──────────┐
               │ PostgreSQL│          │  Redis   │
               └──────────┘          └──────────┘
                    │                       │
                    └───────────┬───────────┘
                                │
                                │ 6.返回结果
                                ▼
                           ┌──────────┐
                           │  前端    │
                           └──────────┘
```

### 3.3 AI计算流程

```
┌──────┐   1.自然语言输入  ┌──────────┐
│ 用户 │ ──────────────→  │  前端    │
└──────┘                   └──────────┘
                                │
                                │ 2.POST /calculate/ai
                                ▼
                           ┌──────────┐
                           │ API服务  │
                           └──────────┘
                                │
                    ┌───────────┴───────────┐
                    │                       │
              3a.调用GLM              3b.检查配额
                    ▼                       ▼
               ┌──────────┐          ┌──────────┐
               │GLM-4.6 API│         │  Redis   │
               └──────────┘          └──────────┘
                    │                       │
                    │ 4.AI理解并生成         │
                    │   数学表达式          │
                    └───────────┬───────────┘
                                │
                                │ 5.执行计算
                                ▼
                           ┌──────────┐
                           │计算引擎  │
                           └──────────┘
                                │
                                │ 6.保存记录
                                ▼
                           ┌──────────┐
                           │ PostgreSQL│
                           └──────────┘
                                │
                                │ 7.返回结果
                                ▼
                           ┌──────────┐
                           │  前端    │
                           └──────────┘
```

## 4. 数据库设计

### 4.1 ER图

```
┌─────────────────┐         ┌─────────────────┐
│     users       │         │    history      │
├─────────────────┤         ├─────────────────┤
│ id (PK)         │◄───┐    │ id (PK)         │
│ username        │    │    │ user_id (FK)    │
│ email           │    └────│ expression      │
│ password_hash   │         │ result          │
│ created_at      │         │ created_at      │
│ updated_at      │         └─────────────────┘
└─────────────────┘                │
                                   │
                                   ▼
                          ┌─────────────────┐
                          │   ai_usage      │
                          ├─────────────────┤
                          │ id (PK)         │
                          │ user_id (FK)    │
                          │ query           │
                          │ tokens_used     │
                          │ created_at      │
                          └─────────────────┘
```

### 4.2 表结构详细设计

#### users 表
```sql
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    username VARCHAR(20) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE,
    is_premium BOOLEAN DEFAULT FALSE
);

CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_username ON users(username);
```

#### history 表
```sql
CREATE TABLE history (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL,
    expression TEXT NOT NULL,
    result VARCHAR(255),
    calculation_type VARCHAR(20) DEFAULT 'basic',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE INDEX idx_history_user_id ON history(user_id);
CREATE INDEX idx_history_created_at ON history(created_at DESC);
CREATE INDEX idx_history_user_created ON history(user_id, created_at DESC);
```

#### ai_usage 表
```sql
CREATE TABLE ai_usage (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL,
    query TEXT NOT NULL,
    tokens_used INTEGER NOT NULL,
    model_version VARCHAR(50) DEFAULT 'glm-4.6',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE INDEX idx_ai_usage_user_id ON ai_usage(user_id);
CREATE INDEX idx_ai_usage_created_at ON ai_usage(created_at DESC);
```

## 5. API设计

### 5.1 API规范

- **协议**: HTTPS
- **版本**: `/api/v1/`
- **认证**: JWT Bearer Token
- **响应格式**: JSON
- **状态码**: RESTful标准

### 5.2 统一响应格式

```json
{
  "code": 200,
  "message": "success",
  "data": {},
  "timestamp": "2025-11-18T10:30:00Z"
}
```

### 5.3 核心API端点

#### 认证模块

**注册用户**
```
POST /api/v1/auth/register
Request:
{
  "username": "testuser",
  "email": "test@example.com",
  "password": "SecurePass123!"
}

Response:
{
  "code": 200,
  "data": {
    "user_id": "uuid-here",
    "username": "testuser",
    "email": "test@example.com"
  }
}
```

**用户登录**
```
POST /api/v1/auth/login
Request:
{
  "email": "test@example.com",
  "password": "SecurePass123!"
}

Response:
{
  "code": 200,
  "data": {
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
    "token_type": "bearer",
    "expires_in": 3600
  }
}
```

#### 计算模块

**基础计算**
```
POST /api/v1/calculate
Headers: Authorization: Bearer {token}
Request:
{
  "expression": "2 + 3 * 4"
}

Response:
{
  "code": 200,
  "data": {
    "expression": "2 + 3 * 4",
    "result": 14,
    "calculation_id": "uuid-here"
  }
}
```

**AI计算**
```
POST /api/v1/calculate/ai
Headers: Authorization: Bearer {token}
Request:
{
  "query": "帮我算123加456"
}

Response:
{
  "code": 200,
  "data": {
    "query": "帮我算123加456",
    "understood": "123 + 456",
    "result": 579,
    "calculation_id": "uuid-here"
  }
}
```

#### 历史记录模块

**获取历史记录**
```
GET /api/v1/history?page=1&page_size=20
Headers: Authorization: Bearer {token}

Response:
{
  "code": 200,
  "data": {
    "items": [
      {
        "id": "uuid",
        "expression": "2 + 3 * 4",
        "result": 14,
        "type": "basic",
        "created_at": "2025-11-18T10:30:00Z"
      }
    ],
    "total": 100,
    "page": 1,
    "page_size": 20
  }
}
```

## 6. 安全架构

### 6.1 认证与授权

- **JWT Token**:
  - 过期时间: 1小时
  - 刷新机制: Refresh Token (7天)
  - 算法: HS256

- **密码安全**:
  - 加密算法: bcrypt
  - Salt轮数: 12
  - 密码强度要求: 8位以上,包含大小写字母和数字

### 6.2 数据安全

- **传输加密**:
  - 强制HTTPS
  - TLS 1.3
  - HSTS头部

- **SQL注入防护**:
  - 使用ORM参数化查询
  - 输入验证和清理
  - 最小权限原则

- **XSS防护**:
  - Content-Security-Policy头部
  - 输入输出转义
  - HttpOnly Cookie

### 6.3 API安全

- **限流策略**:
  - 游客: 10次/分钟
  - 普通用户: 60次/分钟
  - 高级用户: 600次/分钟

- **CORS配置**:
  - 白名单机制
  - 凭证验证
  - 预检请求缓存

## 7. 性能优化

### 7.1 缓存策略

#### Redis缓存
```
计算结果缓存:
  Key: calc:{expression_hash}
  TTL: 1小时
  场景: 重复计算请求

用户会话缓存:
  Key: session:{user_id}
  TTL: 1小时
  场景: 减少数据库查询

限流计数器:
  Key: ratelimit:{user_id}:{minute}
  TTL: 1分钟
  场景: API限流
```

#### 数据库优化
- 索引优化: 为常用查询字段建立索引
- 连接池: 最小5, 最大20连接
- 查询优化: 使用EXPLAIN分析慢查询

### 7.2 前端优化

- **代码分割**: React.lazy + Suspense
- **资源压缩**: Gzip + Brotli
- **CDN加速**: 静态资源使用CDN
- **懒加载**: 图片和组件按需加载

## 8. 可扩展性设计

### 8.1 水平扩展

```
         ┌──────────────┐
         │ Load Balancer│
         └──────────────┘
                │
     ┌──────────┼──────────┐
     │          │          │
┌─────▼────┐ ┌──▼─────┐ ┌──▼─────┐
│ API服务1 │ │API服务2│ │API服务3│
└──────────┘ └────────┘ └────────┘
     │          │          │
     └──────────┼──────────┘
                │
         ┌──────▼──────┐
         │   数据库    │
         │  (主从复制) │
         └────────────┘
```

### 8.2 微服务演进路径

**Phase 1: 单体应用** (当前)
- 所有服务在一个FastAPI应用中

**Phase 2: 服务拆分** (用户>10万)
- 计算服务
- 用户服务
- AI服务

**Phase 3: 微服务** (用户>100万)
- 服务网格 (Istio)
- 消息队列 (RabbitMQ/Kafka)
- 分布式追踪 (Jaeger)

## 9. 监控与日志

### 9.1 监控指标

- **系统指标**: CPU, 内存, 磁盘, 网络
- **应用指标**: QPS, 响应时间, 错误率
- **业务指标**: 活跃用户, 计算次数, AI调用次数

### 9.2 日志规范

```python
# 日志格式
{
  "timestamp": "2025-11-18T10:30:00Z",
  "level": "INFO",
  "service": "api",
  "user_id": "uuid",
  "request_id": "uuid",
  "message": "Calculation completed",
  "duration_ms": 45,
  "metadata": {}
}
```

### 9.3 告警策略

- **P0 (立即响应)**: 服务不可用, 数据丢失
- **P1 (1小时内)**: 错误率>5%, 响应时间>2s
- **P2 (24小时内)**: 磁盘使用>80%, 内存使用>85%

## 10. 部署架构

### 10.1 开发环境

```yaml
# docker-compose.yml
services:
  api:
    build: ./backend/api
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/calculator
      - REDIS_URL=redis://redis:6379

  db:
    image: postgres:14
    volumes:
      - pgdata:/var/lib/postgresql/data

  redis:
    image: redis:7
```

### 10.2 生产环境

```
Kubernetes集群
├── Namespace: production
│   ├── Deployment: api-server (3 replicas)
│   ├── Service: api-service (LoadBalancer)
│   ├── StatefulSet: postgresql (1 master + 2 replicas)
│   ├── StatefulSet: redis (sentinel)
│   ├── ConfigMap: app-config
│   └── Secret: credentials
│
├── Ingress: HTTPS termination
├── HPA: Auto-scaling (2-10 pods)
└── PVC: Persistent storage
```

## 11. 技术债务与改进计划

### 11.1 短期改进 (1-3个月)
- [ ] 实现完整的单元测试覆盖 (目标80%)
- [ ] 添加API文档自动生成
- [ ] 实现前端E2E测试

### 11.2 中期改进 (3-6个月)
- [ ] 引入GraphQL作为备选API
- [ ] 实现WebSocket支持实时计算
- [ ] 添加移动端原生应用

### 11.3 长期规划 (6-12个月)
- [ ] 微服务架构重构
- [ ] 多区域部署
- [ ] AI模型自训练能力

## 12. 参考资料

- **FastAPI文档**: https://fastapi.tiangolo.com/
- **React文档**: https://react.dev/
- **PostgreSQL文档**: https://www.postgresql.org/docs/
- **Redis文档**: https://redis.io/docs/
- **智谱AI文档**: https://open.bigmodel.cn/dev/api
- **Docker文档**: https://docs.docker.com/
- **Kubernetes文档**: https://kubernetes.io/docs/

---

**版本历史**

| 版本 | 日期 | 作者 | 变更说明 |
|------|------|------|----------|
| v1.0 | 2025-11-18 | zuojunwei | 初始版本 |
