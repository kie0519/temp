# Git 远程操作笔记

## 常用远程命令

### 1. 查看远程仓库
```bash
git remote -v              # 查看远程仓库列表
git remote show origin     # 查看详细信息
```

### 2. 获取远程更新
```bash
git fetch origin          # 获取远程更新（不合并）
git fetch --all           # 获取所有远程分支
```

### 3. 拉取远程更新
```bash
git pull origin main      # 拉取并自动合并
git pull                  # 拉取当前分支的远程版本
```

### 4. 推送本地分支
```bash
git push origin main               # 推送到远程 main 分支
git push -u origin feature-branch  # 推送新分支并设置追踪
git push --all                     # 推送所有分支
git push --tags                    # 推送所有标签
```

## fetch vs pull

- **git fetch**: 下载远程更新，但不合并，更安全
- **git pull**: 下载并自动合并，等于 fetch + merge

## 最佳实践

1. 推送前先 pull，避免冲突
2. 使用 fetch 查看远程变化后再决定是否合并
3. 推送新分支时使用 -u 参数设置追踪关系
