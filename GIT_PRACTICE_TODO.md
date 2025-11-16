# Git 练习任务清单

> 📅 开始日期：2025-11-15
> 👤 学习者：kie
> 🎯 目标：掌握 Git 在实际开发中的应用

---

## 📚 第一阶段：基础操作（已完成）

### 1. 仓库初始化与首次提交
- [x] 克隆远程仓库到本地
- [x] 创建项目基础文件（README.md, .gitignore）
- [x] 创建示例代码文件（hello.py）
- [x] 创建 Git 提交规范文档
- [x] 使用 `git add` 添加文件到暂存区
- [x] 使用 `git commit` 创建第一次提交
- [x] 使用 `git push` 推送到远程仓库

**学到的命令：**
```bash
git clone <url> .
git status
git add .
git commit -m "message"
git push -u origin main
```

---

## 📝 第二阶段：日常开发流程

### 2. 修改文件与提交
- [x] 修改 hello.py，添加新功能
- [x] 查看文件改动（git diff）
- [x] 暂存并提交修改
- [x] 推送到远程仓库

**要学习的命令：**
```bash
git diff                    # 查看未暂存的修改
git diff --staged          # 查看已暂存的修改
git add <file>             # 添加指定文件
git commit -m "feat: xxx"  # 提交修改
git push                   # 推送
```

### 3. 查看提交历史
- [x] 查看完整提交历史（git log）
- [x] 查看简洁提交历史（git log --oneline）
- [x] 查看某个文件的修改历史
- [x] 查看特定提交的详细信息（git show）

**要学习的命令：**
```bash
git log
git log --oneline
git log --oneline --graph
git log --follow <file>
git show <commit-hash>
```

### 4. 撤销与修改
- [x] 撤销工作区的修改（git restore）
- [x] 取消暂存的文件（git restore --staged）
- [x] 修改最近一次提交信息（git commit --amend）
- [x] 撤销某次提交（git revert）

**要学习的命令：**
```bash
git checkout -- <file>     # 撤销工作区修改
git reset HEAD <file>      # 取消暂存
git commit --amend         # 修改最近的提交
git revert <commit-hash>   # 撤销指定提交
```

---

## 🌿 第三阶段：分支管理

### 5. 创建和切换分支
- [x] 查看所有分支
- [x] 创建新分支 `feature/add-user-input`
- [x] 切换到新分支
- [x] 在新分支上添加交互式计算器功能
- [x] 提交新功能

**要学习的命令：**
```bash
git branch                      # 查看分支
git branch <branch-name>        # 创建分支
git checkout <branch-name>      # 切换分支
git checkout -b <branch-name>   # 创建并切换分支
git switch <branch-name>        # 切换分支（新命令）
```

### 6. 合并分支
- [x] 切换回 main 分支
- [x] 合并 feature 分支到 main
- [x] 查看合并后的历史
- [x] 删除已合并的 feature 分支

**要学习的命令：**
```bash
git checkout main
git merge <branch-name>
git branch -d <branch-name>    # 删除已合并的分支
git branch -D <branch-name>    # 强制删除分支
```

### 7. 解决合并冲突
- [x] 创建 `feature/modify-greeting` 分支
- [x] 在 main 分支修改 hello.py
- [x] 在 feature 分支也修改同一处代码
- [x] 尝试合并，触发冲突
- [x] 手动解决冲突
- [x] 完成合并提交

**要学习的技能：**
```bash
git merge <branch-name>        # 会提示冲突
# 手动编辑冲突文件，选择保留的代码
git add <resolved-file>
git commit                     # 完成冲突解决
```

---

## 🔄 第四阶段：远程协作

### 8. 远程仓库操作
- [x] 查看远程仓库信息
- [x] 获取远程更新（不合并）
- [x] 拉取远程更新（并合并）
- [x] 推送本地分支到远程

**要学习的命令：**
```bash
git remote -v
git remote show origin
git fetch origin
git pull origin main
git push origin <branch-name>
```

### 9. 多分支协作流程
- [ ] 创建 `develop` 分支作为开发分支
- [ ] 从 develop 创建 `feature/user-input` 分支
- [ ] 开发新功能：接收用户输入
- [ ] 合并到 develop 分支
- [ ] 从 develop 合并到 main
- [ ] 推送所有分支到远程

**要学习的工作流：**
```
main（生产环境）
  ↑
develop（开发环境）
  ↑
feature/xxx（功能分支）
```

### 10. 标签管理
- [x] 为当前版本创建轻量标签
- [x] 创建附注标签（v1.0.0）
- [x] 查看所有标签
- [x] 推送标签到远程
- [x] 查看特定标签的信息

**要学习的命令：**
```bash
git tag v1.0.0
git tag -a v1.0.0 -m "版本 1.0.0"
git tag
git push origin v1.0.0
git push origin --tags
git show v1.0.0
```

---

## 🛠️ 第五阶段：高级操作

### 11. 暂存工作（Stash）
- [ ] 在开发中途需要切换分支
- [ ] 使用 stash 暂存当前工作
- [ ] 切换分支处理其他任务
- [ ] 切换回来恢复暂存的工作
- [ ] 查看和管理 stash 列表

**要学习的命令：**
```bash
git stash
git stash list
git stash pop
git stash apply
git stash drop
git stash clear
```

### 12. 重置提交历史
- [ ] 了解三种重置模式（soft, mixed, hard）
- [ ] 使用 soft 重置保留修改
- [ ] 使用 hard 重置完全回退
- [ ] 使用 reflog 恢复误删的提交

**要学习的命令：**
```bash
git reset --soft HEAD~1    # 软重置
git reset --mixed HEAD~1   # 混合重置（默认）
git reset --hard HEAD~1    # 硬重置
git reflog                 # 查看所有操作记录
```

### 13. 变基操作（Rebase）
- [ ] 创建功能分支并提交多次
- [ ] 使用 rebase 整理提交历史
- [ ] 解决 rebase 过程中的冲突
- [ ] 对比 merge 和 rebase 的区别

**要学习的命令：**
```bash
git rebase main
git rebase -i HEAD~3       # 交互式 rebase
git rebase --continue
git rebase --abort
```

### 14. Cherry-pick（精选提交）
- [ ] 从其他分支挑选特定提交
- [ ] 解决 cherry-pick 冲突
- [ ] 应用多个提交

**要学习的命令：**
```bash
git cherry-pick <commit-hash>
git cherry-pick <hash1> <hash2>
git cherry-pick --continue
git cherry-pick --abort
```

---

## 🎯 第六阶段：实战场景

### 15. 场景一：紧急修复（Hotfix）
- [ ] 模拟生产环境发现 bug
- [ ] 从 main 创建 `hotfix/fix-typo` 分支
- [ ] 快速修复问题
- [ ] 合并到 main 并打标签
- [ ] 同时合并到 develop 分支
- [ ] 推送所有更新

**工作流程：**
```
1. git checkout main
2. git checkout -b hotfix/fix-typo
3. 修复 bug
4. git commit -m "fix: 修复拼写错误"
5. git checkout main
6. git merge hotfix/fix-typo
7. git tag v1.0.1
8. git checkout develop
9. git merge hotfix/fix-typo
10. git push --all && git push --tags
```

### 16. 场景二：功能开发完整流程
- [ ] 从 develop 创建功能分支
- [ ] 多次提交完成功能开发
- [ ] 使用 rebase 整理提交历史
- [ ] 提交前检查代码差异
- [ ] 合并到 develop 进行测试
- [ ] 测试通过后合并到 main
- [ ] 打版本标签并推送

### 17. 场景三：代码回滚
- [ ] 发现某次提交引入了 bug
- [ ] 使用 revert 创建回滚提交
- [ ] 保持提交历史的完整性
- [ ] 推送回滚提交

### 18. 场景四：分支策略实践
- [ ] 实现 Git Flow 工作流
  - main: 生产环境
  - develop: 开发环境
  - feature/*: 功能分支
  - release/*: 发布分支
  - hotfix/*: 热修复分支
- [ ] 模拟完整的发布流程

---

## 🔍 第七阶段：Git 进阶技巧

### 19. Git 配置优化
- [ ] 配置全局用户信息
- [ ] 设置命令别名
- [ ] 配置默认编辑器
- [ ] 配置差异比较工具
- [ ] 了解 .gitconfig 文件

**要学习的命令：**
```bash
git config --global user.name "kie"
git config --global user.email "your@email.com"
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.cm commit
git config --global alias.lg "log --oneline --graph --all"
git config --list
```

### 20. .gitignore 高级用法
- [ ] 忽略特定文件和目录
- [ ] 使用通配符模式
- [ ] 反向忽略（!语法）
- [ ] 调试 .gitignore 规则

**要学习的技巧：**
```bash
git check-ignore -v <file>    # 检查文件被哪条规则忽略
git rm --cached <file>        # 移除已追踪的文件
```

### 21. Git Hooks（钩子）
- [ ] 了解 Git Hooks 的作用
- [ ] 创建 pre-commit 钩子
- [ ] 创建 commit-msg 钩子验证提交信息
- [ ] 使用 Husky 管理钩子（可选）

**钩子位置：** `.git/hooks/`

### 22. 子模块管理（Submodule）
- [ ] 添加子模块到项目
- [ ] 克隆包含子模块的项目
- [ ] 更新子模块
- [ ] 移除子模块

**要学习的命令：**
```bash
git submodule add <url>
git submodule init
git submodule update
git clone --recursive <url>
```

---

## 📊 第八阶段：性能与维护

### 23. 仓库清理与优化
- [ ] 查看仓库大小
- [ ] 清理未追踪的文件
- [ ] 运行垃圾回收
- [ ] 验证仓库完整性

**要学习的命令：**
```bash
git clean -n              # 预览要删除的文件
git clean -fd             # 清理未追踪的文件和目录
git gc                    # 垃圾回收
git fsck                  # 检查仓库完整性
```

### 24. 查找问题提交
- [ ] 使用 git blame 查找代码作者
- [ ] 使用 git bisect 二分查找问题提交
- [ ] 使用 git grep 搜索代码

**要学习的命令：**
```bash
git blame <file>
git bisect start
git bisect bad
git bisect good <commit>
git grep <pattern>
```

---

## 🎓 学习总结与实践

### 25. 综合项目实战
- [ ] 创建一个完整的小项目（待办事项应用）
- [ ] 使用标准分支策略
- [ ] 编写规范的提交信息
- [ ] 创建多个版本标签
- [ ] 模拟多人协作场景
- [ ] 编写项目的 CHANGELOG

### 26. 最佳实践清单
- [ ] 经常提交，保持原子性
- [ ] 写清晰的提交信息
- [ ] 提交前检查代码差异
- [ ] 定期推送到远程仓库
- [ ] 使用分支进行功能开发
- [ ] 及时删除已合并的分支
- [ ] 为重要版本打标签
- [ ] 不提交敏感信息（密码、密钥等）
- [ ] 保持 .gitignore 更新

---

## 📈 进度统计

- **总任务数：** 26 个大任务
- **已完成：** 10 ✅
- **进行中：** 0 🔄
- **未开始：** 16 ⏳
- **完成度：** 38.5%

---

## 📚 参考资源

- [Pro Git 中文版](https://git-scm.com/book/zh/v2)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Git Flow 工作流](https://nvie.com/posts/a-successful-git-branching-model/)
- [GitHub Docs](https://docs.github.com/)
- [Learn Git Branching](https://learngitbranching.js.org/?locale=zh_CN) - 可视化学习

---

## 💡 学习建议

1. **循序渐进：** 按照阶段顺序学习，不要跳过
2. **多练习：** 每个命令至少实践 3 次
3. **记笔记：** 记录常用命令和遇到的问题
4. **犯错没关系：** Git 几乎所有操作都可以撤销
5. **查文档：** 使用 `git help <command>` 查看详细文档
6. **实际应用：** 在真实项目中应用所学知识

---

**最后更新：** 2025-11-15
**下一步计划：** 开始第二阶段的日常开发流程练习
