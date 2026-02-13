# 大型备份文件处理指南

## 问题说明
- 当前备份文件 `openclaw-backup-2026-02-13.tar.gz` 大小为 2GB
- GitHub 单文件限制为 100MB（普通文件）或 2GB（LFS）
- 直接上传到 GitHub 不可行

## 解决方案

### 方案 1: 使用 GitHub Releases（推荐）
```bash
# 1. 创建一个新的 GitHub Release
# 2. 在 Release 页面上传大文件
# 3. 文件将通过 GitHub 的 CDN 分发，可直接下载
```

### 方案 2: 优化备份内容
```bash
# 只备份必要的配置文件，排除大型日志和缓存
tar -czf openclaw-config-backup-$(date +%Y-%m-%d).tar.gz \
    --exclude='*.log' \
    --exclude='.cache' \
    --exclude='workspace/knowledge/youtube/*' \
    -C /home/codespace/.openclaw .
```

### 方案 3: 文件分割
```bash
# 将大文件分割成 100MB 的块
split -b 100M openclaw-backup-2026-02-13.tar.gz openclaw-backup-part-

# 上传各部分到 GitHub，然后在恢复时合并
# cat openclaw-backup-part-* > openclaw-backup-restored.tar.gz
```

## 推荐做法
1. 保留当前 2GB 文件作为本地完整备份
2. 创建一个精简版配置备份（<100MB）用于 GitHub 存储
3. 使用 GitHub Releases 功能上传完整的 2GB 备份