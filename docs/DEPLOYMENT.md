# 部署指南

## 快速开始

本指南将帮助您在本地环境部署智能计算器应用。

## 环境要求

### 必需
- Python 3.8+
- Node.js 18+
- npm 或 yarn

### 可选
- PostgreSQL 14+ (推荐,默认使用 SQLite)
- Redis 7+ (缓存,可选)
- 智谱 AI API Key (AI 计算功能)

## 后端部署

### 1. 安装依赖

```bash
cd backend/api
pip install -r requirements.txt
```

### 2. 配置环境变量

复制 `.env.example` 并修改:

```bash
cp ../../.env.example .env
```

编辑 `.env` 文件:

```bash
# 数据库配置 (默认 SQLite)
DATABASE_URL=sqlite:///./calculator.db

# 或使用 PostgreSQL
# DATABASE_URL=postgresql://user:password@localhost:5432/calculator

# JWT 密钥 (生产环境务必修改!)
SECRET_KEY=your-super-secret-key-change-in-production

# 智谱 AI API Key (可选,用于 AI 计算)
GLM_API_KEY=your-glm-api-key-here

# CORS 允许的源
CORS_ORIGINS=http://localhost:3000,http://localhost:5173
```

### 3. 初始化数据库

```bash
python init_db.py init
```

输出:
```
✅ 数据库表已创建
```

### 4. 启动后端服务

```bash
python app.py
```

或使用 uvicorn:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

服务启动在 `http://localhost:8000`

### 5. 验证后端

访问 API 文档:
- Swagger: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

健康检查:
```bash
curl http://localhost:8000/health
# 响应: {"status":"healthy"}
```

## 前端部署

### 1. 安装依赖

```bash
cd frontend/web
npm install
```

或使用 yarn:

```bash
yarn install
```

### 2. 启动开发服务器

```bash
npm run dev
```

服务启动在 `http://localhost:5173`

Vite 会自动代理 `/api` 请求到后端 `http://localhost:8000`

### 3. 构建生产版本

```bash
npm run build
```

构建产物在 `dist/` 目录

### 4. 预览生产版本

```bash
npm run preview
```

## 完整启动流程

### 终端 1 - 后端

```bash
cd backend/api
python app.py
```

### 终端 2 - 前端

```bash
cd frontend/web
npm run dev
```

### 访问应用

打开浏览器访问: http://localhost:5173

## 使用指南

### 1. 注册账号

1. 点击页面上的"立即注册"
2. 填写用户名 (3-20字符)
3. 填写邮箱
4. 设置密码 (至少8字符,包含大小写字母和数字)
5. 点击"注册"

### 2. 登录

1. 输入邮箱和密码
2. 点击"登录"
3. 自动跳转到计算器页面

### 3. 基础计算

1. 确保"AI 模式"开关关闭
2. 在"数学表达式"输入框输入,例如: `2 + 3 * 4`
3. 点击"计算"或按 Enter
4. 查看计算结果

支持的运算:
- 基本运算: `+`, `-`, `*`, `/`, `**`, `%`
- 函数: `sqrt()`, `sin()`, `cos()`, `tan()`, `log()`, `exp()`, `abs()`, `pow()`
- 常量: `pi`, `e`, `tau`

示例:
```
2 + 3 * 4          → 14
sqrt(16)           → 4
sin(pi/2)          → 1
pow(2, 10)         → 1024
```

### 4. AI 计算 (需要配置 API Key)

1. 打开"AI 模式"开关
2. 在输入框用自然语言描述,例如: "帮我算123加456"
3. 点击"AI 计算"
4. AI 会理解并显示提取的表达式和结果

示例查询:
- "帮我算100的平方根"
- "2的10次方是多少"
- "sin30度等于多少"

### 5. 查看历史

1. 点击顶部菜单的"历史记录"
2. 查看所有计算历史
3. 可以删除单条记录或清空所有

## 生产环境部署

### 使用 Docker (推荐)

创建 `docker-compose.yml`:

```yaml
version: '3.8'

services:
  postgres:
    image: postgres:14
    environment:
      POSTGRES_DB: calculator
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
    volumes:
      - pgdata:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  backend:
    build: ./backend/api
    environment:
      DATABASE_URL: postgresql://user:password@postgres:5432/calculator
      SECRET_KEY: ${SECRET_KEY}
      GLM_API_KEY: ${GLM_API_KEY}
      CORS_ORIGINS: https://yourdomain.com
    ports:
      - "8000:8000"
    depends_on:
      - postgres

  frontend:
    build: ./frontend/web
    ports:
      - "80:80"
    depends_on:
      - backend

volumes:
  pgdata:
```

启动:
```bash
docker-compose up -d
```

### 使用 Nginx

前端构建后,配置 Nginx:

```nginx
server {
    listen 80;
    server_name yourdomain.com;

    # 前端静态文件
    location / {
        root /var/www/calculator-web/dist;
        try_files $uri $uri/ /index.html;
    }

    # API 代理
    location /api {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### 使用 Gunicorn (生产级 WSGI)

```bash
cd backend/api
gunicorn app:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

## 常见问题

### Q1: 后端启动失败 - ModuleNotFoundError

**问题**: `ModuleNotFoundError: No module named 'xxx'`

**解决**:
```bash
pip install -r requirements.txt
```

### Q2: 前端启动失败 - Cannot find module

**问题**: `Error: Cannot find module 'xxx'`

**解决**:
```bash
rm -rf node_modules package-lock.json
npm install
```

### Q3: API 请求失败 - CORS 错误

**问题**: `Access to XMLHttpRequest has been blocked by CORS policy`

**解决**: 在后端 `.env` 文件添加前端地址:
```bash
CORS_ORIGINS=http://localhost:5173
```

### Q4: 数据库连接失败

**问题**: `sqlalchemy.exc.OperationalError`

**解决**:
1. 检查 PostgreSQL 是否启动
2. 检查 `DATABASE_URL` 配置是否正确
3. 或使用默认的 SQLite: `DATABASE_URL=sqlite:///./calculator.db`

### Q5: AI 计算失败 - AI服务未配置

**问题**: `AI服务未配置, 请联系管理员`

**解决**: 在 `.env` 文件配置智谱 API Key:
```bash
GLM_API_KEY=your-api-key-here
```

获取 API Key: https://open.bigmodel.cn/

### Q6: JWT Token 过期

**问题**: 操作时提示"无效的认证凭证"

**解决**: Token 默认1小时过期,重新登录即可

### Q7: 前端构建失败 - TypeScript 错误

**问题**: `TS2307: Cannot find module '@/xxx'`

**解决**: 检查 `tsconfig.json` 中的路径别名配置,确保 `vite.config.ts` 正确配置

### Q8: 端口被占用

**问题**: `Error: listen EADDRINUSE: address already in use :::8000`

**解决**:
```bash
# 查找占用进程
lsof -i :8000  # macOS/Linux
netstat -ano | findstr :8000  # Windows

# 杀死进程
kill -9 <PID>  # macOS/Linux
taskkill /PID <PID> /F  # Windows

# 或更换端口
uvicorn app:app --port 8001
```

## 性能优化建议

### 后端优化

1. **使用 PostgreSQL 替代 SQLite**
   ```bash
   DATABASE_URL=postgresql://user:pass@localhost:5432/calculator
   ```

2. **启用 Redis 缓存**
   ```python
   # 缓存计算结果
   redis_client.setex(f"calc:{expr_hash}", 3600, result)
   ```

3. **使用连接池**
   ```python
   engine = create_engine(
       DATABASE_URL,
       pool_size=20,
       max_overflow=10
   )
   ```

4. **启用 Gunicorn 多进程**
   ```bash
   gunicorn app:app -w 4  # 4个worker进程
   ```

### 前端优化

1. **启用代码分割**
   ```tsx
   const HistoryPage = lazy(() => import('./pages/HistoryPage'));
   ```

2. **使用 CDN**
   ```html
   <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/antd/dist/antd.min.css">
   ```

3. **启用 Gzip 压缩** (Nginx)
   ```nginx
   gzip on;
   gzip_types text/plain text/css application/json application/javascript;
   ```

4. **使用服务端渲染 (SSR)**
   - 考虑迁移到 Next.js

## 监控和日志

### 后端日志

使用 Python logging:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='app.log'
)
```

### 前端错误监控

使用 Sentry:

```tsx
import * as Sentry from "@sentry/react";

Sentry.init({
  dsn: "your-sentry-dsn",
  integrations: [new Sentry.BrowserTracing()],
  tracesSampleRate: 1.0,
});
```

### 性能监控

使用 Prometheus + Grafana:

```python
from prometheus_client import Counter, Histogram

request_count = Counter('http_requests_total', 'Total HTTP Requests')
request_duration = Histogram('http_request_duration_seconds', 'HTTP Request Duration')
```

## 备份和恢复

### 数据库备份

```bash
# PostgreSQL
pg_dump calculator > backup.sql

# 恢复
psql calculator < backup.sql
```

### 文件备份

```bash
# 备份整个项目
tar -czf calculator-backup-$(date +%Y%m%d).tar.gz temp/

# 恢复
tar -xzf calculator-backup-20250118.tar.gz
```

## 升级指南

### 1. 备份数据

```bash
python init_db.py backup
```

### 2. 拉取最新代码

```bash
git pull origin main
```

### 3. 更新依赖

```bash
cd backend/api
pip install -r requirements.txt --upgrade

cd ../../frontend/web
npm update
```

### 4. 迁移数据库

```bash
python init_db.py migrate
```

### 5. 重启服务

```bash
# 重启后端
systemctl restart calculator-backend

# 重新构建前端
npm run build
```

## 安全建议

1. **使用 HTTPS**
   - 配置 SSL 证书 (Let's Encrypt)

2. **修改默认密钥**
   - 生成强随机 `SECRET_KEY`

3. **限制 CORS**
   - 只允许可信域名

4. **使用环境变量**
   - 不要在代码中硬编码密钥

5. **定期更新依赖**
   ```bash
   pip list --outdated
   npm outdated
   ```

6. **启用防火墙**
   ```bash
   ufw allow 80/tcp
   ufw allow 443/tcp
   ufw enable
   ```

## 支持

如有问题,请:
- 查看 [API 使用指南](api/API_USAGE.md)
- 查看 [系统架构文档](design/architecture.md)
- 提交 Issue: https://github.com/kie0519/temp/issues

---

**文档版本**: v1.0
**最后更新**: 2025-11-18
**作者**: zuojunwei
