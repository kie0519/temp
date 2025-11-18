# Git 配置优化指南

## 配置层级

Git 有三个配置层级（优先级从高到低）：

1. **本地配置** (仓库级别): `.git/config`
2. **全局配置** (用户级别): `~/.gitconfig`
3. **系统配置** (系统级别): `/etc/gitconfig`

## 查看配置

```bash
# 查看所有配置
git config --list

# 查看配置及其来源
git config --list --show-origin

# 查看特定配置
git config user.name
git config user.email

# 查看全局配置
git config --global --list
```

## 基础配置

### 1. 用户信息

```bash
# 配置用户名和邮箱（必需）
git config --global user.name "zuojunwei"
git config --global user.email "junwei.zuo@aminer.cn"
```

### 2. 默认编辑器

```bash
# 设置 VS Code 为默认编辑器
git config --global core.editor "code --wait"

# 或使用 vim
git config --global core.editor "vim"

# 或使用 nano
git config --global core.editor "nano"
```

### 3. 默认分支名称

```bash
# 设置默认分支为 main（而不是 master）
git config --global init.defaultBranch main
```

## 命令别名

本项目已配置的别名：

```bash
# 常用命令简写
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.cm commit

# 查看最后一次提交
git config --global alias.last 'log -1 HEAD'

# 美化的提交历史
git config --global alias.lg 'log --oneline --graph --all --decorate'

# 取消暂存
git config --global alias.unstage 'reset HEAD --'

# 可视化工具
git config --global alias.visual '!gitk'
```

### 使用别名

```bash
# 原命令            # 别名
git status      →  git st
git checkout    →  git co
git branch      →  git br
git commit      →  git cm
git log         →  git lg
```

## 更多实用别名

```bash
# 查看差异（带词级别高亮）
git config --global alias.df 'diff --word-diff'

# 显示所有别名
git config --global alias.aliases '!git config --get-regexp ^alias\.'

# 撤销上次提交（保留修改）
git config --global alias.undo 'reset HEAD~1 --mixed'

# 修改上次提交
git config --global alias.amend 'commit --amend --no-edit'

# 查看贡献者统计
git config --global alias.contributors 'shortlog -sn'

# 显示分支关系图
git config --global alias.tree 'log --graph --oneline --all'
```

## 颜色配置

```bash
# 启用彩色输出
git config --global color.ui auto

# 自定义颜色
git config --global color.status.changed "yellow"
git config --global color.status.untracked "red"
git config --global color.branch.current "green bold"
```

## 性能优化

```bash
# 启用文件系统缓存（Windows）
git config --global core.fscache true

# 启用并行处理
git config --global core.preloadindex true

# 增加 HTTP 缓冲区大小
git config --global http.postBuffer 524288000
```

## 行尾符配置

```bash
# Windows 用户（自动转换）
git config --global core.autocrlf true

# Mac/Linux 用户
git config --global core.autocrlf input

# 不转换（不推荐）
git config --global core.autocrlf false
```

## 差异工具和合并工具

```bash
# 配置 VS Code 作为差异工具
git config --global diff.tool vscode
git config --global difftool.vscode.cmd 'code --wait --diff $LOCAL $REMOTE'

# 配置 VS Code 作为合并工具
git config --global merge.tool vscode
git config --global mergetool.vscode.cmd 'code --wait $MERGED'
```

## 其他实用配置

```bash
# 推送时自动设置上游分支
git config --global push.autoSetupRemote true

# 拉取时使用 rebase 而不是 merge
git config --global pull.rebase true

# 启用凭证缓存（15分钟）
git config --global credential.helper 'cache --timeout=900'

# 忽略文件权限变化
git config --global core.fileMode false
```

## 查看和编辑配置文件

```bash
# 直接编辑全局配置文件
git config --global --edit

# 查看配置文件位置
git config --global --list --show-origin
```

## 删除配置

```bash
# 删除特定配置
git config --global --unset user.name

# 删除整个配置段
git config --global --remove-section alias
```

## 本项目当前配置

### 用户信息
- **用户名**: 左俊威 (zuojunwei)
- **邮箱**: junwei.zuo@aminer.cn

### 编辑器
- **默认编辑器**: VS Code

### 已配置别名
| 别名 | 完整命令 | 说明 |
|------|---------|------|
| `st` | status | 查看状态 |
| `co` | checkout | 切换分支 |
| `br` | branch | 分支管理 |
| `cm` | commit | 提交 |
| `last` | log -1 HEAD | 最后一次提交 |
| `lg` | log --oneline --graph --all --decorate | 美化历史 |
| `unstage` | reset HEAD -- | 取消暂存 |
| `visual` | !gitk | 可视化工具 |

## 配置文件示例

```ini
[user]
    name = zuojunwei
    email = junwei.zuo@aminer.cn

[core]
    editor = code --wait
    autocrlf = true

[alias]
    st = status
    co = checkout
    br = branch
    cm = commit
    lg = log --oneline --graph --all --decorate
    last = log -1 HEAD
    unstage = reset HEAD --

[color]
    ui = auto

[push]
    autoSetupRemote = true

[pull]
    rebase = true
```

## 最佳实践

1. ✅ **始终配置用户名和邮箱**
2. ✅ **使用别名提高效率**
3. ✅ **配置合适的编辑器**
4. ✅ **启用彩色输出**
5. ✅ **根据操作系统配置行尾符**
6. ✅ **定期备份配置文件**

## 参考资源

- [Git 配置官方文档](https://git-scm.com/docs/git-config)
- [Pro Git - 配置 Git](https://git-scm.com/book/zh/v2/自定义-Git-配置-Git)

---

**创建日期**: 2025-11-17
**作者**: zuojunwei
