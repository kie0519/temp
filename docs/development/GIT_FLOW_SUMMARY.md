# Git Flow 工作流总结

## 什么是 Git Flow？

Git Flow 是一种广泛使用的 Git 分支管理策略，由 Vincent Driessen 提出。它定义了一个围绕项目发布的严格分支模型。

## 分支类型

### 1. 主要分支（长期存在）

#### main (master)
- **用途**: 生产环境代码
- **特点**: 始终保持稳定可发布状态
- **来源**: 从 release 或 hotfix 分支合并
- **标签**: 每次合并后打版本标签

#### develop
- **用途**: 开发环境代码
- **特点**: 包含最新的开发功能
- **来源**: 从 feature 分支合并
- **作用**: 作为 feature 分支的基础

### 2. 辅助分支（临时存在）

#### feature/* (功能分支)
- **从哪创建**: develop
- **合并到哪**: develop
- **命名**: feature/功能名称
- **生命周期**: 功能开发期间
- **示例**: feature/math-constants (任务 16)

#### hotfix/* (热修复分支)
- **从哪创建**: main
- **合并到哪**: main 和 develop
- **命名**: hotfix/修复描述
- **生命周期**: 紧急修复期间
- **示例**: hotfix/urgent-readme-fix (任务 15)

#### release/* (发布分支)
- **从哪创建**: develop
- **合并到哪**: main 和 develop
- **命名**: release/版本号
- **生命周期**: 发布准备期间
- **用途**: 版本准备、bug 修复、文档更新

## 完整工作流程

### 功能开发流程（Feature）
```bash
# 1. 从 develop 创建功能分支
git checkout develop
git checkout -b feature/new-feature

# 2. 开发并提交
git add .
git commit -m "feat: 添加新功能"

# 3. 完成后合并回 develop
git checkout develop
git merge feature/new-feature

# 4. 删除功能分支
git branch -d feature/new-feature
```

### 发布流程（Release）
```bash
# 1. 从 develop 创建发布分支
git checkout develop
git checkout -b release/v1.2.0

# 2. 准备发布（更新版本号、文档等）
git commit -m "chore: 准备 v1.2.0 发布"

# 3. 合并到 main
git checkout main
git merge release/v1.2.0
git tag -a v1.2.0 -m "版本 1.2.0"

# 4. 合并回 develop
git checkout develop
git merge release/v1.2.0

# 5. 删除发布分支
git branch -d release/v1.2.0

# 6. 推送
git push --all
git push --tags
```

### 热修复流程（Hotfix）
```bash
# 1. 从 main 创建热修复分支
git checkout main
git checkout -b hotfix/critical-bug

# 2. 修复问题
git commit -m "fix: 修复紧急 bug"

# 3. 合并到 main
git checkout main
git merge hotfix/critical-bug
git tag -a v1.0.1 -m "紧急修复版本"

# 4. 合并到 develop
git checkout develop
git merge hotfix/critical-bug

# 5. 删除热修复分支
git branch -d hotfix/critical-bug

# 6. 推送
git push --all
git push --tags
```

## 版本号规范（Semantic Versioning）

格式：**主版本号.次版本号.修订号** (MAJOR.MINOR.PATCH)

- **主版本号 (MAJOR)**: 不兼容的 API 修改
- **次版本号 (MINOR)**: 向下兼容的功能性新增
- **修订号 (PATCH)**: 向下兼容的问题修正

示例：
- v1.0.0 → v1.0.1 (hotfix)
- v1.0.1 → v1.1.0 (feature)
- v1.1.0 → v2.0.0 (breaking change)

## 本项目实践记录

### 任务 15：Hotfix 流程
- 分支: hotfix/urgent-readme-fix
- 问题: README 缺少学习进度信息
- 版本: v1.0.0 → v1.0.1
- 流程: main → hotfix → main + develop

### 任务 16：Feature 流程
- 分支: feature/math-constants
- 功能: 数学常量模块
- 版本: v1.0.1 → v1.1.0
- 流程: develop → feature → develop → main

### 任务 17：代码回滚
- 操作: git revert
- 场景: 移除了除零检查的错误提交
- 分支: develop
- 结果: 保持历史完整性的回滚

## Git Flow 优缺点

### 优点
✅ 清晰的分支结构
✅ 适合版本化发布的项目
✅ 支持并行开发
✅ 明确的发布流程
✅ 便于回滚和问题追踪

### 缺点
❌ 对于持续部署项目过于复杂
❌ 需要维护多个长期分支
❌ 学习曲线较陡

## 替代方案

- **GitHub Flow**: 简化版，只有 main 和 feature 分支
- **GitLab Flow**: 介于 Git Flow 和 GitHub Flow 之间
- **Trunk Based Development**: 基于主干的开发

## 最佳实践

1. **频繁合并**: 避免长期存在的分支
2. **代码审查**: 合并前进行 PR/MR review
3. **自动化**: 使用 CI/CD 自动化测试和部署
4. **保护分支**: 对 main 和 develop 设置保护规则
5. **清理分支**: 及时删除已合并的分支
6. **规范命名**: 使用一致的分支命名规则
7. **标签管理**: 每次发布都打标签

## 参考资源

- [A successful Git branching model](https://nvie.com/posts/a-successful-git-branching-model/)
- [Git Flow Cheatsheet](https://danielkummer.github.io/git-flow-cheatsheet/)
- [Semantic Versioning](https://semver.org/)

---

**创建日期**: 2025-11-17
**作者**: zuojunwei
