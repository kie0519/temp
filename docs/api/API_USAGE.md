# API 使用指南

## 快速开始

### 1. 启动 API 服务

```bash
cd backend/api
python app.py
```

服务将在 `http://localhost:8000` 启动

### 2. 访问 API 文档

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API 端点概览

### 认证模块 (`/api/v1/auth`)

| 方法 | 端点 | 描述 | 需要认证 |
|------|------|------|---------|
| POST | `/auth/register` | 用户注册 | ❌ |
| POST | `/auth/login` | 用户登录 | ❌ |
| GET | `/auth/me` | 获取当前用户信息 | ✅ |

### 计算模块 (`/api/v1/calculate`)

| 方法 | 端点 | 描述 | 需要认证 |
|------|------|------|---------|
| POST | `/calculate` | 基础计算 | ✅ |
| POST | `/calculate/validate` | 验证表达式 | ✅ |
| POST | `/calculate/ai` | AI 智能计算 | ✅ |

### 历史记录模块 (`/api/v1/history`)

| 方法 | 端点 | 描述 | 需要认证 |
|------|------|------|---------|
| GET | `/history` | 获取历史记录 (分页) | ✅ |
| DELETE | `/history/{id}` | 删除单条记录 | ✅ |
| DELETE | `/history` | 清空历史记录 | ✅ |
| GET | `/history/stats/ai-usage` | AI 使用统计 | ✅ |

## 完整使用流程

### 步骤 1: 用户注册

```bash
curl -X POST "http://localhost:8000/api/v1/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser",
    "email": "test@example.com",
    "password": "TestPass123"
  }'
```

**响应示例:**

```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "username": "testuser",
  "email": "test@example.com",
  "is_active": true,
  "is_premium": false,
  "created_at": "2025-11-18T10:30:00Z",
  "updated_at": "2025-11-18T10:30:00Z"
}
```

### 步骤 2: 用户登录

```bash
curl -X POST "http://localhost:8000/api/v1/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "TestPass123"
  }'
```

**响应示例:**

```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "token_type": "bearer",
  "expires_in": 3600,
  "user": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "username": "testuser",
    "email": "test@example.com",
    "is_active": true,
    "is_premium": false,
    "created_at": "2025-11-18T10:30:00Z",
    "updated_at": "2025-11-18T10:30:00Z"
  }
}
```

**保存 token** 用于后续请求

### 步骤 3: 基础计算

```bash
curl -X POST "http://localhost:8000/api/v1/calculate" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -d '{
    "expression": "2 + 3 * 4"
  }'
```

**响应示例:**

```json
{
  "expression": "2 + 3 * 4",
  "result": 14.0,
  "calculation_id": "7c9e6679-7425-40de-944b-e07fc1f90ae7"
}
```

### 步骤 4: AI 智能计算 (需要 GLM API Key)

```bash
curl -X POST "http://localhost:8000/api/v1/calculate/ai" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -d '{
    "query": "帮我算123加456"
  }'
```

**响应示例:**

```json
{
  "query": "帮我算123加456",
  "understood": "123 + 456",
  "result": 579.0,
  "calculation_id": "8d4f7890-8536-51ef-a55c-f18gd2g01bf8",
  "tokens_used": 150
}
```

### 步骤 5: 查看历史记录

```bash
curl -X GET "http://localhost:8000/api/v1/history?page=1&page_size=10" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

**响应示例:**

```json
{
  "items": [
    {
      "id": "8d4f7890-8536-51ef-a55c-f18gd2g01bf8",
      "expression": "123 + 456",
      "result": "579",
      "calculation_type": "ai",
      "created_at": "2025-11-18T10:35:00Z"
    },
    {
      "id": "7c9e6679-7425-40de-944b-e07fc1f90ae7",
      "expression": "2 + 3 * 4",
      "result": "14",
      "calculation_type": "basic",
      "created_at": "2025-11-18T10:32:00Z"
    }
  ],
  "total": 2,
  "page": 1,
  "page_size": 10,
  "total_pages": 1
}
```

### 步骤 6: 获取 AI 使用统计

```bash
curl -X GET "http://localhost:8000/api/v1/history/stats/ai-usage" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

**响应示例:**

```json
{
  "total_queries": 5,
  "total_tokens": 750
}
```

## 支持的数学运算

### 基本运算符

- `+` 加法
- `-` 减法
- `*` 乘法
- `/` 除法
- `**` 幂运算
- `%` 取模
- `//` 整除

### 数学函数

| 函数 | 说明 | 示例 | 结果 |
|------|------|------|------|
| `sin(x)` | 正弦 | `sin(pi/2)` | 1.0 |
| `cos(x)` | 余弦 | `cos(0)` | 1.0 |
| `tan(x)` | 正切 | `tan(pi/4)` | 1.0 |
| `sqrt(x)` | 平方根 | `sqrt(16)` | 4.0 |
| `log(x)` | 自然对数 | `log(e)` | 1.0 |
| `log10(x)` | 常用对数 | `log10(100)` | 2.0 |
| `exp(x)` | 指数 | `exp(1)` | 2.718... |
| `abs(x)` | 绝对值 | `abs(-5)` | 5.0 |
| `pow(x, y)` | 幂运算 | `pow(2, 10)` | 1024.0 |

### 数学常量

- `pi` - 圆周率 (3.14159...)
- `e` - 自然常数 (2.71828...)
- `tau` - 2π (6.28318...)

## 错误处理

### HTTP 状态码

| 状态码 | 说明 |
|--------|------|
| 200 | 请求成功 |
| 201 | 创建成功 |
| 204 | 删除成功 (无内容) |
| 400 | 请求参数错误 |
| 401 | 未认证 |
| 403 | 权限不足 |
| 404 | 资源不存在 |
| 500 | 服务器内部错误 |
| 503 | 服务不可用 (如 AI 服务未配置) |

### 错误响应格式

```json
{
  "detail": "错误信息描述"
}
```

### 常见错误示例

**1. 未提供认证令牌**

```json
{
  "detail": "Not authenticated"
}
```

**2. 令牌已过期**

```json
{
  "detail": "无效的认证凭证"
}
```

**3. 表达式语法错误**

```json
{
  "detail": "表达式语法错误: invalid syntax"
}
```

**4. 除零错误**

```json
{
  "detail": "除数不能为零"
}
```

**5. AI 服务未配置**

```json
{
  "detail": "AI服务未配置, 请联系管理员"
}
```

## 认证说明

### JWT Token 生命周期

- **有效期**: 1 小时 (3600 秒)
- **算法**: HS256
- **Payload**: `{"sub": "用户ID", "username": "用户名", "exp": "过期时间"}`

### 使用 Token

在所有需要认证的请求中,添加 HTTP 头部:

```
Authorization: Bearer {your_access_token}
```

### Token 刷新

目前版本不支持 Refresh Token,Token 过期后需要重新登录。

## Python 客户端示例

```python
import requests

# 基础配置
BASE_URL = "http://localhost:8000/api/v1"

# 1. 注册
register_response = requests.post(
    f"{BASE_URL}/auth/register",
    json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "TestPass123"
    }
)
print("注册:", register_response.json())

# 2. 登录
login_response = requests.post(
    f"{BASE_URL}/auth/login",
    json={
        "email": "test@example.com",
        "password": "TestPass123"
    }
)
token = login_response.json()["access_token"]
print("Token:", token)

# 3. 创建认证头
headers = {"Authorization": f"Bearer {token}"}

# 4. 基础计算
calc_response = requests.post(
    f"{BASE_URL}/calculate",
    headers=headers,
    json={"expression": "sqrt(16) + pow(2, 3)"}
)
print("计算结果:", calc_response.json())

# 5. AI 计算
ai_response = requests.post(
    f"{BASE_URL}/calculate/ai",
    headers=headers,
    json={"query": "帮我算100的平方根"}
)
print("AI 结果:", ai_response.json())

# 6. 查看历史
history_response = requests.get(
    f"{BASE_URL}/history?page=1&page_size=5",
    headers=headers
)
print("历史记录:", history_response.json())
```

## JavaScript 客户端示例

```javascript
const BASE_URL = 'http://localhost:8000/api/v1';
let token = '';

// 1. 注册
async function register() {
  const response = await fetch(`${BASE_URL}/auth/register`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      username: 'testuser',
      email: 'test@example.com',
      password: 'TestPass123'
    })
  });
  const data = await response.json();
  console.log('注册:', data);
}

// 2. 登录
async function login() {
  const response = await fetch(`${BASE_URL}/auth/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      email: 'test@example.com',
      password: 'TestPass123'
    })
  });
  const data = await response.json();
  token = data.access_token;
  console.log('Token:', token);
}

// 3. 计算
async function calculate(expression) {
  const response = await fetch(`${BASE_URL}/calculate`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    },
    body: JSON.stringify({ expression })
  });
  const data = await response.json();
  console.log('结果:', data);
  return data;
}

// 4. AI 计算
async function aiCalculate(query) {
  const response = await fetch(`${BASE_URL}/calculate/ai`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    },
    body: JSON.stringify({ query })
  });
  const data = await response.json();
  console.log('AI 结果:', data);
  return data;
}

// 使用示例
(async () => {
  await register();
  await login();
  await calculate('2 + 3 * 4');
  await aiCalculate('帮我算123加456');
})();
```

## 环境变量配置

创建 `.env` 文件:

```bash
# 数据库配置
DATABASE_URL=sqlite:///./calculator.db
# 或使用 PostgreSQL:
# DATABASE_URL=postgresql://user:password@localhost:5432/calculator

# JWT 密钥 (生产环境必须修改!)
SECRET_KEY=your-super-secret-key-change-in-production

# 智谱 AI API Key (可选,用于 AI 计算)
GLM_API_KEY=your-glm-api-key-here
GLM_API_BASE=https://open.bigmodel.cn/api/paas/v4

# CORS 允许的源 (逗号分隔)
CORS_ORIGINS=http://localhost:3000,http://localhost:5173
```

## 数据库初始化

```bash
cd backend/api

# 初始化数据库 (创建表)
python init_db.py init

# 重置数据库 (删除并重新创建)
python init_db.py reset

# 删除所有表
python init_db.py drop
```

## 测试建议

### 使用 Swagger UI 测试

1. 访问 http://localhost:8000/docs
2. 点击 "Authorize" 按钮
3. 输入格式: `Bearer {your_token}`
4. 现在可以直接在页面上测试所有 API

### 使用 Postman

1. 创建新的 Collection
2. 添加环境变量: `base_url` = `http://localhost:8000/api/v1`
3. 创建登录请求,保存 token 到环境变量
4. 在其他请求的 Header 中使用 `{{token}}`

### 使用 curl

参考上面的 curl 示例,替换 `YOUR_TOKEN_HERE` 为实际的 token

## 性能建议

1. **使用连接池**: 生产环境建议配置数据库连接池
2. **启用缓存**: 频繁计算的表达式可以缓存结果
3. **限流**: 建议添加 API 限流中间件
4. **异步处理**: AI 计算较慢,可以考虑异步队列
5. **监控**: 添加日志和监控,追踪 API 性能

## 下一步

- [ ] 实现 Refresh Token 机制
- [ ] 添加 API 限流
- [ ] 实现结果缓存 (Redis)
- [ ] 添加单元测试
- [ ] 实现 WebSocket 支持
- [ ] 添加批量计算接口
- [ ] 实现导出功能 (CSV/Excel)
- [ ] 添加管理员后台

---

**版本**: v0.1.0
**最后更新**: 2025-11-18
**作者**: zuojunwei
