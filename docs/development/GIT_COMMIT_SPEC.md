# Git Commit 提交规范

## Conventional Commits 规范（推荐）

这是目前最广泛使用的提交规范，被 Google、Angular、Vue.js 等大厂采用。

### 提交格式

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Type 类型说明

| 类型 | 说明 | 示例 |
|------|------|------|
| **feat** | 新功能 | feat(auth): 添加用户登录功能 |
| **fix** | 修复 bug | fix(api): 修复数据获取失败的问题 |
| **docs** | 文档修改 | docs(readme): 更新安装说明 |
| **style** | 代码格式（不影响代码运行） | style: 统一代码缩进格式 |
| **refactor** | 重构（既不是新功能也不是修复 bug） | refactor(utils): 重构日期处理函数 |
| **perf** | 性能优化 | perf(query): 优化数据库查询性能 |
| **test** | 测试相关 | test(user): 添加用户模块单元测试 |
| **build** | 构建系统或外部依赖变更 | build: 升级 webpack 到 5.0 |
| **ci** | CI 配置文件和脚本变更 | ci: 添加 GitHub Actions 工作流 |
| **chore** | 其他不修改 src 或测试文件的变更 | chore: 更新 .gitignore 文件 |
| **revert** | 回退之前的 commit | revert: 回退 feat(auth) 提交 |

### Scope 范围（可选）

表示本次提交影响的范围，例如：
- `auth` - 认证模块
- `api` - API 接口
- `ui` - 用户界面
- `db` - 数据库
- `config` - 配置文件

### Subject 主题

- 使用现在时态（"添加功能" 而不是 "已添加功能"）
- 首字母小写
- 结尾不加句号
- 简洁明了，不超过 50 字符

### Body 正文（可选）

- 详细描述本次提交的内容
- 说明为什么做这个改动
- 如何解决问题

### Footer 页脚（可选）

- 关联 Issue：`Closes #123`
- 破坏性变更：`BREAKING CHANGE: 说明`

## 完整示例

### 示例 1：新功能
```
feat(auth): 添加 JWT 用户认证功能

实现基于 JWT 的用户认证系统，包括：
- 用户登录接口
- 密码加密存储
- Token 生成和验证

Closes #123
```

### 示例 2：修复 Bug
```
fix(api): 修复用户数据获取失败的问题

当用户 ID 不存在时，API 返回 500 错误。
现在改为返回 404 并提供友好的错误信息。

Fixes #456
```

### 示例 3：文档更新
```
docs(readme): 更新项目安装说明

- 添加 Node.js 版本要求
- 补充环境变量配置步骤
- 修正命令行示例错误
```

### 示例 4：性能优化
```
perf(database): 优化用户查询性能

添加数据库索引，将平均查询时间从 500ms 降低到 50ms。
```

## Angular 规范（Google）

```
<type>(<scope>): <short summary>
  │       │             │
  │       │             └─⫸ 现在时态，不大写，结尾无句号
  │       │
  │       └─⫸ Commit Scope: 影响范围
  │
  └─⫸ Commit Type: build|ci|docs|feat|fix|perf|refactor|test
```

### 规则：
- Subject 不超过 100 字符
- Body 每行不超过 100 字符
- 使用英文或项目主要语言

## 国内大厂规范

### 阿里巴巴
- 遵循 Conventional Commits
- 中英文混合项目建议使用英文
- 单行不超过 100 字符
- 提交信息要清晰说明改动原因

### 腾讯
- 采用 Conventional Commits
- 注重中文可读性
- 要求关联需求或 Bug ID

### 字节跳动
- 严格遵循 Conventional Commits
- 配合工具自动生成 CHANGELOG
- 强制使用 commitlint 检查

## 最佳实践

### 1. 提交频率
- 每个独立的功能或修复单独提交
- 不要把多个不相关的改动放在一起
- 经常提交，保持提交历史清晰

### 2. 提交信息质量
- ✅ 好的提交：`feat(user): 添加用户头像上传功能`
- ❌ 差的提交：`update`, `fix bug`, `修改`

### 3. 原子性提交
每次提交应该是一个完整的、可工作的改动：
```bash
# 好的实践
git commit -m "feat(auth): 添加登录功能"
git commit -m "test(auth): 添加登录功能的单元测试"

# 避免
git commit -m "一些修改"  # 包含了登录、注册、个人资料等多个功能
```

### 4. 使用工具辅助

#### Commitizen（交互式提交）
```bash
npm install -g commitizen
git cz  # 替代 git commit
```

#### Commitlint（提交信息检查）
```bash
npm install --save-dev @commitlint/cli @commitlint/config-conventional
```

#### Husky（Git Hooks）
```bash
npm install --save-dev husky
npx husky install
```

## 常用命令

```bash
# 查看提交历史
git log --oneline

# 查看某个文件的提交历史
git log --follow filename

# 查看提交详情
git show commit-hash

# 修改最近的提交信息
git commit --amend

# 查看简洁的提交历史
git log --pretty=format:"%h - %an, %ar : %s"
```

## 参考资源

- [Conventional Commits 官网](https://www.conventionalcommits.org/)
- [Angular Commit Guidelines](https://github.com/angular/angular/blob/main/CONTRIBUTING.md)
- [阿里巴巴开发规范](https://github.com/alibaba/p3c)
