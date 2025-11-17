# Git Hooks 完整指南

## 什么是 Git Hooks？

Git Hooks（钩子）是 Git 在特定事件发生时自动执行的脚本。它们允许你在 Git 工作流的关键点自动化任务，如代码检查、测试运行、提交信息验证等。

## Hooks 的位置

所有 Git Hooks 脚本都存储在项目的 `.git/hooks/` 目录中。

```bash
# 查看 hooks 目录
ls -la .git/hooks/

# Git 默认提供了示例脚本（.sample 文件）
.git/hooks/
├── pre-commit.sample
├── commit-msg.sample
├── pre-push.sample
└── ...
```

## Hooks 的类型

### 客户端 Hooks（本地操作）

#### 1. pre-commit

**触发时机**：在执行 `git commit` 之前，还未输入提交信息时

**用途**：
- 检查代码格式（Linting）
- 运行代码风格检查
- 检查是否有未解决的 TODO/FIXME
- 检查是否包含敏感信息（密码、密钥）
- 运行单元测试

**示例脚本**：
```bash
#!/bin/sh
# .git/hooks/pre-commit

echo "运行 pre-commit 钩子..."

# 检查是否有敏感信息
if git diff --cached | grep -E "password|secret|API_KEY"; then
    echo "❌ 错误：提交中包含敏感信息！"
    exit 1
fi

# 运行代码格式检查（Python 示例）
if command -v black &> /dev/null; then
    echo "检查 Python 代码格式..."
    black --check .
    if [ $? -ne 0 ]; then
        echo "❌ 代码格式不符合规范，请运行 'black .' 格式化代码"
        exit 1
    fi
fi

echo "✅ pre-commit 检查通过！"
exit 0
```

**如何跳过**：
```bash
# 使用 --no-verify 跳过 pre-commit hook
git commit --no-verify -m "紧急修复"
```

---

#### 2. prepare-commit-msg

**触发时机**：在提交信息编辑器打开之前，但在默认信息生成之后

**用途**：
- 自动添加提交模板
- 根据分支名添加前缀
- 添加 issue 号

**示例脚本**：
```bash
#!/bin/sh
# .git/hooks/prepare-commit-msg

COMMIT_MSG_FILE=$1
COMMIT_SOURCE=$2

# 获取当前分支名
BRANCH_NAME=$(git symbolic-ref --short HEAD)

# 如果是 feature 分支，自动添加前缀
if [[ $BRANCH_NAME == feature/* ]]; then
    FEATURE_NAME=$(echo $BRANCH_NAME | sed 's/feature\///')
    echo "feat($FEATURE_NAME): " > $COMMIT_MSG_FILE.tmp
    cat $COMMIT_MSG_FILE >> $COMMIT_MSG_FILE.tmp
    mv $COMMIT_MSG_FILE.tmp $COMMIT_MSG_FILE
fi
```

---

#### 3. commit-msg

**触发时机**：在用户输入提交信息之后，提交完成之前

**用途**：
- 验证提交信息格式
- 检查提交信息是否符合规范
- 确保提交信息包含必要的信息（如 issue 号）

**示例脚本**（验证 Conventional Commits 格式）：
```bash
#!/bin/sh
# .git/hooks/commit-msg

COMMIT_MSG_FILE=$1
COMMIT_MSG=$(cat $COMMIT_MSG_FILE)

# Conventional Commits 正则表达式
PATTERN="^(feat|fix|docs|style|refactor|test|chore)(\(.+\))?: .{1,50}"

if ! echo "$COMMIT_MSG" | grep -qE "$PATTERN"; then
    echo "❌ 提交信息格式错误！"
    echo ""
    echo "正确格式："
    echo "  <type>(<scope>): <subject>"
    echo ""
    echo "示例："
    echo "  feat(auth): 添加用户登录功能"
    echo "  fix(api): 修复数据获取错误"
    echo "  docs: 更新 README"
    echo ""
    exit 1
fi

echo "✅ 提交信息格式正确！"
exit 0
```

---

#### 4. post-commit

**触发时机**：在提交完成之后

**用途**：
- 发送通知
- 更新文档
- 触发 CI/CD（虽然通常由远程 hooks 处理）

**示例脚本**：
```bash
#!/bin/sh
# .git/hooks/post-commit

echo "📧 提交成功！正在发送通知..."
# 这里可以添加通知逻辑
```

---

#### 5. pre-push

**触发时机**：在执行 `git push` 之前

**用途**：
- 运行完整的测试套件
- 检查是否推送到正确的分支
- 防止推送到受保护的分支

**示例脚本**：
```bash
#!/bin/sh
# .git/hooks/pre-push

BRANCH_NAME=$(git symbolic-ref --short HEAD)

# 禁止直接推送到 main 分支
if [ "$BRANCH_NAME" = "main" ]; then
    echo "❌ 禁止直接推送到 main 分支！"
    echo "请创建 Pull Request 进行代码审查。"
    exit 1
fi

# 运行测试
echo "运行测试..."
npm test
if [ $? -ne 0 ]; then
    echo "❌ 测试失败，推送已取消"
    exit 1
fi

echo "✅ pre-push 检查通过！"
exit 0
```

---

#### 6. post-merge

**触发时机**：在 `git merge` 成功之后

**用途**：
- 自动安装依赖（如 package.json 改变后运行 npm install）
- 清理临时文件
- 更新数据库迁移

**示例脚本**：
```bash
#!/bin/sh
# .git/hooks/post-merge

# 检查 package.json 是否改变
if git diff --name-only HEAD@{1} HEAD | grep -q "package.json"; then
    echo "📦 package.json 已改变，正在安装依赖..."
    npm install
fi
```

---

### 服务端 Hooks（远程仓库）

#### 1. pre-receive

**触发时机**：在接收推送之前

**用途**：
- 验证推送的提交
- 检查权限
- 拒绝不符合规范的推送

---

#### 2. update

**触发时机**：为每个推送的分支单独触发

**用途**：
- 分支级别的访问控制
- 强制执行分支命名规范

---

#### 3. post-receive

**触发时机**：在推送完成之后

**用途**：
- 触发 CI/CD 流程
- 发送通知邮件
- 自动部署

---

## 创建和使用 Hooks

### 方法一：手动创建

```bash
# 1. 进入 hooks 目录
cd .git/hooks/

# 2. 创建 hook 脚本（无 .sample 后缀）
touch pre-commit

# 3. 添加可执行权限
chmod +x pre-commit

# 4. 编辑脚本内容
vim pre-commit
```

### 方法二：使用工具管理

#### Husky（推荐，Node.js 项目）

Husky 是最流行的 Git Hooks 管理工具，它将 hooks 脚本版本化。

```bash
# 安装 Husky
npm install --save-dev husky

# 初始化 Husky
npx husky install

# 添加 pre-commit hook
npx husky add .husky/pre-commit "npm test"

# 添加 commit-msg hook
npx husky add .husky/commit-msg 'npx --no -- commitlint --edit "$1"'
```

**package.json 配置**：
```json
{
  "scripts": {
    "prepare": "husky install"
  },
  "devDependencies": {
    "husky": "^8.0.0",
    "commitlint": "^17.0.0"
  }
}
```

#### pre-commit（Python 项目）

```bash
# 安装 pre-commit
pip install pre-commit

# 创建配置文件 .pre-commit-config.yaml
cat > .pre-commit-config.yaml <<EOF
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
EOF

# 安装 hooks
pre-commit install
```

---

## 实战示例

### 示例 1：代码格式化检查

```bash
#!/bin/sh
# .git/hooks/pre-commit

# Python 项目
if command -v black &> /dev/null; then
    black --check .
fi

# JavaScript 项目
if command -v prettier &> /dev/null; then
    prettier --check .
fi

# Java 项目
if command -v google-java-format &> /dev/null; then
    google-java-format --dry-run --set-exit-if-changed $(find . -name "*.java")
fi
```

### 示例 2：提交信息验证

```bash
#!/bin/sh
# .git/hooks/commit-msg

COMMIT_MSG=$(cat $1)

# 检查长度
if [ ${#COMMIT_MSG} -lt 10 ]; then
    echo "❌ 提交信息太短（至少 10 个字符）"
    exit 1
fi

# 检查格式
if ! echo "$COMMIT_MSG" | grep -qE "^(feat|fix|docs|style|refactor|test|chore)"; then
    echo "❌ 提交信息必须以 feat/fix/docs/style/refactor/test/chore 开头"
    exit 1
fi

exit 0
```

### 示例 3：自动运行测试

```bash
#!/bin/sh
# .git/hooks/pre-push

echo "🧪 运行测试..."

# Python 项目
if [ -f "pytest.ini" ]; then
    pytest
    TEST_RESULT=$?
fi

# Node.js 项目
if [ -f "package.json" ]; then
    npm test
    TEST_RESULT=$?
fi

# 检查测试结果
if [ $TEST_RESULT -ne 0 ]; then
    echo "❌ 测试失败，推送已取消"
    exit 1
fi

echo "✅ 所有测试通过！"
exit 0
```

### 示例 4：防止提交敏感信息

```bash
#!/bin/sh
# .git/hooks/pre-commit

# 敏感关键词列表
SENSITIVE_PATTERNS=(
    "password"
    "api_key"
    "API_KEY"
    "secret"
    "SECRET"
    "token"
    "TOKEN"
    "private_key"
    "PRIVATE_KEY"
)

# 检查暂存的文件
for pattern in "${SENSITIVE_PATTERNS[@]}"; do
    if git diff --cached | grep -i "$pattern"; then
        echo "❌ 警告：检测到可能的敏感信息：$pattern"
        echo "请检查你的代码，确保没有提交密码、密钥等敏感信息"
        exit 1
    fi
done

echo "✅ 未检测到敏感信息"
exit 0
```

---

## 调试 Hooks

### 1. 添加调试输出

```bash
#!/bin/sh
# 添加 set -x 显示每条命令
set -x

echo "开始执行 hook..."
# 你的代码
```

### 2. 查看 Hook 执行日志

```bash
# 手动执行 hook 查看输出
.git/hooks/pre-commit

# 或者
sh -x .git/hooks/pre-commit
```

### 3. 临时禁用 Hook

```bash
# 方法 1：重命名
mv .git/hooks/pre-commit .git/hooks/pre-commit.disabled

# 方法 2：使用 --no-verify
git commit --no-verify -m "消息"
git push --no-verify
```

---

## 最佳实践

### 1. ✅ 使用工具管理 Hooks

**推荐使用**：Husky（Node.js）、pre-commit（Python）

**优点**：
- Hooks 脚本可以版本控制
- 团队成员自动获得相同的 hooks
- 更容易维护和更新

### 2. ✅ Hooks 应该快速执行

```bash
# ❌ 不好：运行完整的测试套件
#!/bin/sh
pytest tests/  # 可能需要几分钟

# ✅ 好：只运行快速检查
#!/bin/sh
flake8 .       # 几秒钟
black --check .
```

### 3. ✅ 提供友好的错误信息

```bash
# ❌ 不好
echo "Error"
exit 1

# ✅ 好
echo "❌ 错误：提交信息格式不正确"
echo ""
echo "正确格式：<type>: <subject>"
echo "示例：feat: 添加用户登录功能"
exit 1
```

### 4. ✅ 允许跳过 Hooks

```bash
# 在紧急情况下允许跳过
git commit --no-verify -m "紧急修复"
```

### 5. ✅ 文档化你的 Hooks

在项目的 README 中说明：
- 有哪些 hooks
- 每个 hook 做什么
- 如何安装/配置
- 如何跳过（如果需要）

### 6. ✅ Hooks 应该是幂等的

多次运行同一个 hook 应该产生相同的结果。

### 7. ✅ 不要在 Hooks 中进行破坏性操作

```bash
# ❌ 危险：自动修改文件
black .
git add .

# ✅ 安全：只检查，让用户自己修复
black --check .
if [ $? -ne 0 ]; then
    echo "请运行 'black .' 格式化代码"
    exit 1
fi
```

---

## 常见问题

### Q1: 为什么我的 Hook 没有执行？

**可能的原因**：
1. Hook 文件没有执行权限
   ```bash
   chmod +x .git/hooks/pre-commit
   ```

2. Hook 文件名错误（不应有 .sample 后缀）
   ```bash
   # ❌ 错误
   .git/hooks/pre-commit.sample

   # ✅ 正确
   .git/hooks/pre-commit
   ```

3. Hook 脚本有语法错误
   ```bash
   # 手动执行检查
   sh -x .git/hooks/pre-commit
   ```

### Q2: 如何在团队中共享 Hooks？

**.git/hooks/** 目录不会被 Git 跟踪，建议：

**方案 1：使用 Husky**
```bash
npm install --save-dev husky
npx husky install
```

**方案 2：脚本安装**
```bash
# 将 hooks 放在项目目录中
project/
├── scripts/
│   └── hooks/
│       └── pre-commit
└── .git/

# 创建安装脚本
# setup-hooks.sh
cp scripts/hooks/* .git/hooks/
chmod +x .git/hooks/*
```

### Q3: Hooks 可以用其他语言编写吗？

可以！只要脚本是可执行的。

**Python 示例**：
```python
#!/usr/bin/env python3
# .git/hooks/pre-commit

import sys
import subprocess

result = subprocess.run(['pytest'], capture_output=True)
sys.exit(result.returncode)
```

**Node.js 示例**：
```javascript
#!/usr/bin/env node
// .git/hooks/pre-commit

const { execSync } = require('child_process');

try {
    execSync('npm test', { stdio: 'inherit' });
    process.exit(0);
} catch (error) {
    process.exit(1);
}
```

---

## 实用 Hooks 资源

### Husky + lint-staged（推荐）

只对暂存的文件运行 linters：

```bash
npm install --save-dev husky lint-staged

# package.json
{
  "lint-staged": {
    "*.js": ["eslint --fix", "prettier --write"],
    "*.py": ["black", "flake8"],
    "*.md": ["prettier --write"]
  }
}
```

### commitlint（提交信息检查）

```bash
npm install --save-dev @commitlint/cli @commitlint/config-conventional

# commitlint.config.js
module.exports = {
  extends: ['@commitlint/config-conventional']
};

# 配置 hook
npx husky add .husky/commit-msg 'npx --no -- commitlint --edit "$1"'
```

---

## 总结

### Hooks 的价值

✅ **自动化重复任务**：格式化、测试、检查
✅ **提高代码质量**：强制执行规范
✅ **防止错误**：在提交前捕获问题
✅ **团队协作**：统一开发流程

### 关键要点

1. **客户端 Hooks**：在本地执行（pre-commit, commit-msg, pre-push）
2. **服务端 Hooks**：在远程仓库执行（pre-receive, post-receive）
3. **使用工具**：Husky, pre-commit 等
4. **保持快速**：不要阻塞开发者
5. **提供反馈**：清晰的错误信息

### 下一步

- 在实际项目中配置 Hooks
- 尝试 Husky 或 pre-commit 工具
- 建立团队的 Hooks 规范
- 持续优化和改进

---

**参考资源**：
- [Git 官方文档 - Hooks](https://git-scm.com/book/zh/v2/自定义-Git-Git-钩子)
- [Husky 官方文档](https://typicode.github.io/husky/)
- [pre-commit 官方文档](https://pre-commit.com/)
- [commitlint 文档](https://commitlint.js.org/)

---

**创建日期**: 2025-11-17
**作者**: zuojunwei
