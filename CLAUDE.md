# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

这是一个用于学习和实践 Git 版本控制的教学项目。项目的主要目的是系统性地学习 Git 操作，从基础到高级，涵盖 26 个大任务，分为 8 个学习阶段。当前完成度：53.8% (14/26)。

**学习者：** kie (zuojunwei)
**仓库地址：** https://github.com/kie0519/temp.git

## 工作语言和规范

### 提交规范
- **必须使用中文进行 Git commit**
- 严格遵循 Conventional Commits 规范（详见 [GIT_COMMIT_SPEC.md](GIT_COMMIT_SPEC.md)）
- 提交格式：`<type>(<scope>): <subject>`
- 每次提交必须包含署名：`Co-Authored-By: zuojunwei`
- **不要**包含 Claude Code 相关的署名或链接

### 提交类型 (Type)
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
docs: 完成任务 XX - 任务名称

本次学习内容：
- 学习点 1
- 学习点 2

更新进度：XX.X% (X/26)

Co-Authored-By: zuojunwei
EOF
)"
```

## 项目结构

```
.
├── .gitignore              # Git 忽略规则
├── GIT_COMMIT_SPEC.md      # Git 提交规范（Conventional Commits）
├── GIT_PRACTICE_TODO.md    # 26 个学习任务清单（跟踪进度）
├── REMOTE_NOTES.md         # 远程操作笔记
├── README.md               # 项目说明
└── hello.py                # Python 示例代码（数学计算器工具集）
```

## 核心文件说明

### GIT_PRACTICE_TODO.md
- **最重要的文件**，包含完整的 26 个学习任务
- 分为 8 个阶段：基础操作 → 日常开发 → 分支管理 → 远程协作 → 高级操作 → 实战场景 → 进阶技巧 → 性能维护
- 每个任务完成后，**必须**更新此文件中的复选框和进度统计
- 进度统计格式：`已完成：X ✅` 和 `完成度：XX.X%`

### hello.py
- 演示文件，用于 Git 操作练习
- 包含多个数学计算函数（加减乘除、幂运算、取模、平方根、绝对值）
- 包含交互式计算器功能
- 在学习过程中会持续修改此文件以演示各种 Git 操作

## 学习任务执行流程

当用户说"继续"时，应该：

1. **查看当前进度**：读取 GIT_PRACTICE_TODO.md，找到下一个未完成的任务
2. **使用 TodoWrite 工具**：将任务分解为多个步骤并跟踪
3. **执行任务**：
   - 创建必要的分支、文件、提交
   - 演示相关 Git 命令
   - 解释操作的意义和效果
4. **更新进度**：
   - 标记 GIT_PRACTICE_TODO.md 中的复选框为 `[x]`
   - 更新进度统计（已完成数和百分比）
5. **提交并推送**：
   - 使用规范的中文提交信息
   - 署名 `Co-Authored-By: zuojunwei`
   - 推送到远程仓库

## Git 操作最佳实践

### 分支策略
- `main`: 主分支，用于稳定版本
- `feature/*`: 功能分支，用于开发新功能
- `hotfix/*`: 热修复分支，用于紧急修复
- `develop`: 开发分支（某些任务中使用）

### 演示用分支
- 在演示完成后，应该删除演示用的分支
- 使用 `git branch -d` 删除已合并分支
- 使用 `git branch -D` 强制删除未合并分支

### 冲突解决
- 在演示冲突时，手动编辑文件解决冲突
- 移除冲突标记 `<<<<<<<`, `=======`, `>>>>>>>`
- 标记冲突已解决后继续操作

## 已完成的学习任务（1-14）

1. ✅ 仓库初始化与首次提交
2. ✅ 修改文件与提交
3. ✅ 查看提交历史
4. ✅ 撤销与修改
5. ✅ 创建和切换分支
6. ✅ 合并分支
7. ✅ 解决合并冲突
8. ✅ 远程仓库操作
9. ⏳ 多分支协作流程
10. ✅ 标签管理
11. ✅ 暂存工作（Stash）
12. ✅ 重置提交历史（Reset）
13. ✅ 变基操作（Rebase）
14. ✅ Cherry-pick（精选提交）

## 下一步任务

下一个待完成任务是：**任务 15 - 场景一：紧急修复（Hotfix）**

这是实战场景阶段的第一个任务，将模拟真实的生产环境 bug 修复流程。

## 运行代码

```bash
# 运行 Python 示例程序
python hello.py

# 或使用 Python 3
python3 hello.py
```

## 常用 Git 命令参考

```bash
# 查看状态和历史
git status
git log --oneline --graph --all
git reflog

# 分支操作
git branch
git checkout -b <branch-name>
git merge <branch-name>
git branch -d <branch-name>

# 远程操作
git fetch origin
git pull
git push
git push --tags

# 高级操作
git stash / git stash pop
git reset --soft/--mixed/--hard
git rebase <branch>
git cherry-pick <commit-hash>

# 撤销操作
git restore <file>
git revert <commit>
git reset HEAD~1
```

## 重要提醒

1. **所有 commit 必须使用中文**
2. **署名必须是 zuojunwei，不要包含 Claude 相关内容**
3. **每完成一个任务，必须更新 GIT_PRACTICE_TODO.md**
4. **使用 TodoWrite 工具跟踪任务进度**
5. **演示分支在使用后应删除，保持仓库整洁**
6. **推送前确认所有文件修改都已提交**
