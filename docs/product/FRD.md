# FRD - 功能需求文档  
# Functional Requirement Document

**项目名称**: 智能计算器  
**文档版本**: v1.0  
**创建日期**: 2025-11-17  
**技术负责人**: zuojunwei  

---

## 1. API 接口设计

### 1.1 基础计算接口

**POST /api/v1/calculate**

请求:
```json
{
  "expression": "2 + 3 * 4"
}
```

响应:
```json
{
  "code": 200,
  "data": {
    "result": 14
  }
}
```

### 1.2 AI 计算接口

**POST /api/v1/calculate/ai**

请求:
```json
{
  "query": "帮我算123加456"
}
```

响应:
```json
{
  "code": 200,
  "data": {
    "result": 579,
    "understood": "123 + 456"
  }
}
```

---

## 2. 数据库设计

### 2.1 用户表
```sql
CREATE TABLE users (
    id UUID PRIMARY KEY,
    username VARCHAR(20) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 2.2 历史记录表
```sql
CREATE TABLE history (
    id UUID PRIMARY KEY,
    user_id UUID NOT NULL,
    expression TEXT NOT NULL,
    result VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

---

## 3. 业务逻辑

### 3.1 计算流程
1. 接收表达式
2. 解析验证
3. 执行计算
4. 保存历史
5. 返回结果

### 3.2 AI 计算流程
1. 接收自然语言
2. 调用 GLM API
3. 解析结果
4. 执行计算
5. 记录使用量
6. 返回结果

---

## 4. 安全设计

- JWT 认证
- bcrypt 密码加密
- SQL 注入防护
- XSS 防护
- CSRF Token

---

## 5. 性能要求

| 指标 | 目标 |
|------|------|
| API 响应 | < 100ms |
| AI 响应 | < 2s |
| 并发 | 10,000+ |

---

**审批**: zuojunwei - 2025-11-17
