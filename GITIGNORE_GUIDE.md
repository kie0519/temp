# .gitignore 高级用法指南

## 什么是 .gitignore？

`.gitignore` 文件用于告诉 Git 哪些文件或目录不需要添加到版本控制中。

## 基本语法

```bash
# 这是注释

# 忽略特定文件
secrets.txt

# 忽略特定目录（结尾加斜杠）
node_modules/

# 忽略特定扩展名的所有文件
*.log
*.tmp

# 忽略特定模式的文件
test_*
```

## 通配符模式

### 1. 星号（*）- 匹配任意字符

```bash
# 忽略所有 .log 文件
*.log

# 忽略所有以 test 开头的文件
test*

# 忽略所有以 .bak 结尾的文件
*.bak
```

### 2. 问号（?）- 匹配单个字符

```bash
# 匹配 test1.txt, test2.txt，但不匹配 test10.txt
test?.txt

# 匹配 file1.log, fileA.log
file?.log
```

### 3. 双星号（**）- 匹配任意中间目录

```bash
# 匹配所有目录下的 debug.log
**/debug.log

# 匹配 logs 下所有子目录的 *.log
logs/**/*.log

# 匹配所有 temp 目录
**/temp/
```

### 4. 方括号（[]）- 匹配字符范围

```bash
# 匹配 test1.txt 到 test9.txt
test[0-9].txt

# 匹配 testA.txt, testB.txt, testC.txt
test[ABC].txt

# 匹配 test-a.txt, test-b.txt
test-[a-z].txt
```

## 反向忽略（! 语法）

使用 `!` 可以排除某些文件不被忽略：

```bash
# 忽略所有 .txt 文件
*.txt

# 但不忽略 README.txt
!README.txt

# 但不忽略 docs/ 目录下的 .txt 文件
!docs/*.txt
```

### 重要规则

1. **顺序很重要**：后面的规则可以覆盖前面的规则
2. **不能反向忽略已忽略目录中的文件**：

```bash
# 这样不行
logs/
!logs/important.log  # 无效，因为整个 logs/ 已被忽略

# 正确做法
logs/*
!logs/important.log  # 有效
```

## 目录特定规则

### 只忽略根目录

```bash
# 只忽略根目录的 config.txt
/config.txt

# 但不忽略子目录的 config.txt
# 例如：src/config.txt 不会被忽略
```

### 忽略所有层级

```bash
# 忽略所有 temp 目录
temp/

# 或者
**/temp/
```

## 实用命令

### 1. 检查文件是否被忽略

```bash
# 检查文件是否被忽略
git check-ignore filename.txt

# 显示是哪条规则导致忽略（-v 详细模式）
git check-ignore -v filename.txt
```

### 2. 列出所有被忽略的文件

```bash
# 显示所有被忽略的文件
git status --ignored

# 简洁模式
git status --ignored --short
```

### 3. 移除已跟踪的文件

如果文件已经被 Git 跟踪，添加到 .gitignore 后需要：

```bash
# 从 Git 中移除但保留本地文件
git rm --cached filename.txt

# 移除整个目录
git rm -r --cached directory/

# 提交更改
git commit -m "chore: 更新 .gitignore"
```

### 4. 强制添加被忽略的文件

```bash
# 强制添加被忽略的文件
git add -f important.log
```

## 常见模式示例

### Python 项目

```bash
# 字节码
__pycache__/
*.py[cod]
*$py.class

# 虚拟环境
venv/
env/
ENV/
.venv

# 包文件
*.egg-info/
dist/
build/

# IDE
.vscode/
.idea/
*.swp
```

### Node.js 项目

```bash
# 依赖
node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# 构建输出
dist/
build/
.next/
out/

# 环境变量
.env
.env.local
.env.*.local

# IDE
.vscode/
.idea/
```

### Java 项目

```bash
# 编译文件
*.class
*.jar
*.war
*.ear

# 构建目录
target/
build/
out/

# IDE
.idea/
*.iml
.classpath
.project
.settings/
```

## 高级技巧

### 1. 组合规则

```bash
# 忽略所有 .log 文件
*.log

# 但保留根目录的 important.log
!/important.log

# 忽略 build 目录下的所有内容
build/*

# 但保留 build/README.md
!build/README.md
```

### 2. 临时文件模式

```bash
# 编辑器临时文件
*~
*.swp
*.swo
.*.sw?

# 操作系统文件
.DS_Store
Thumbs.db
desktop.ini

# 临时文件
*.tmp
*.temp
*.bak
*.backup
```

### 3. 环境和配置

```bash
# 环境变量（包含敏感信息）
.env
.env.local
.env.*.local

# 但保留示例文件
!.env.example

# 配置文件
config.local.js
settings.local.json

# 但保留默认配置
!config.default.js
```

## 调试技巧

### 查看匹配的规则

```bash
# 查看文件被哪条规则忽略
git check-ignore -v file.txt

# 输出示例：
# .gitignore:15:*.txt    file.txt
# 表示：文件名:行号:规则    匹配的文件
```

### 测试模式

```bash
# 创建测试文件
touch test1.txt test2.log important.txt

# 查看状态
git status --short

# 检查每个文件
git check-ignore -v test1.txt
git check-ignore -v test2.log
git check-ignore -v important.txt
```

## 本项目的 .gitignore

当前项目包含的忽略规则：

### 基础规则
- Python 字节码和虚拟环境
- Node.js 依赖
- IDE 配置文件
- 操作系统文件
- 临时文件
- 环境变量文件

### 高级规则示例
- 通配符模式：`*.backup`, `test?.txt`
- 双星号：`logs/**/debug.log`
- 反向忽略：`!important.txt`
- 目录规则：`/build/`, `**/temp/`

## 最佳实践

1. ✅ **尽早添加** .gitignore
2. ✅ **分组注释**：按类型组织规则
3. ✅ **使用模板**：参考 [gitignore.io](https://gitignore.io)
4. ✅ **测试规则**：使用 `git check-ignore`
5. ✅ **不提交敏感信息**：`.env`, `secrets.json`
6. ✅ **不提交构建产物**：`dist/`, `build/`
7. ✅ **不提交依赖**：`node_modules/`, `vendor/`
8. ✅ **提交 .gitignore**：让团队共享规则

## 全局 .gitignore

为所有仓库设置全局忽略规则：

```bash
# 创建全局 .gitignore
touch ~/.gitignore_global

# 配置 Git 使用它
git config --global core.excludesfile ~/.gitignore_global

# 添加全局规则（IDE、OS 文件等）
echo ".DS_Store" >> ~/.gitignore_global
echo "Thumbs.db" >> ~/.gitignore_global
echo ".vscode/" >> ~/.gitignore_global
```

## 参考资源

- [Git 官方文档 - gitignore](https://git-scm.com/docs/gitignore)
- [GitHub .gitignore 模板](https://github.com/github/gitignore)
- [gitignore.io](https://gitignore.io) - 生成 .gitignore 文件
- [Git 忽略文件原理](https://git-scm.com/book/zh/v2/Git-基础-记录每次更新到仓库)

---

**创建日期**: 2025-11-17
**作者**: zuojunwei
