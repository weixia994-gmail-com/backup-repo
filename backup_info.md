# 备份文件说明

## 当前备份状态

### 1. 轻量级备份
- **文件**: openclaw-accurate-backup-2026-02-13.tar.gz
- **大小**: 88MB
- **内容**: OpenClaw 配置和数据的精简备份
- **用途**: 适用于快速恢复基本系统配置

### 2. Filemail 备份
- **链接**: https://www.filemail.com/d/gvajeoreschicaz
- **说明**: 包含额外知识库和媒体文件的完整备份
- **注意**: 该链接可能包含比 88MB 备份更多的内容

## 推荐备份策略
1. **日常备份**: 使用 88MB 的轻量级备份（已存储在 GitHub）
2. **完整备份**: 使用 Filemail 链接访问完整备份
3. **备份频率**: 建议每周进行一次轻量级备份

## 备份脚本
```bash
# 创建轻量级备份
cd /home/codespace && tar -czf openclaw-accurate-backup-$(date +%Y-%m-%d).tar.gz -C /home/codespace .openclaw
```

## 文件大小说明
- 原始 `.openclaw` 目录大小: 95MB
- 实际备份文件大小: 88MB (经过压缩)
- 之前 2GB 文件为误操作产生，包含重复内容