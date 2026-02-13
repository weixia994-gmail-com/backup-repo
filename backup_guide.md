# OpenClaw 系统备份指南

## 1. 备份目的
- 定期备份 OpenClaw 系统配置和数据
- 防止意外数据丢失
- 便于系统迁移和恢复

## 2. 备份文件详情
- **文件名**: openclaw-backup-2026-02-13.tar.gz
- **大小**: 192MB
- **内容**: 包含 .openclaw 目录和 /workspaces/clawdbot 目录
- **创建时间**: 2026-02-13

## 3. 备份文件生成命令
```bash
# 在 Codespace 终端执行
cd ~
tar -czvf openclaw-backup-$(date +%F).tar.gz .openclaw /workspaces/clawdbot
```

## 4. 备份内容
- `.openclaw` 目录下的所有配置文件
  - 认证信息和令牌
  - 模型配置
  - 工作空间设置
  - 历史记录和日志
- `/workspaces/clawdbot` 目录
  - 项目文件
  - 自定义脚本
  - 配置文件

## 5. 推送到远程仓库
```bash
# 将备份文件复制到仓库
cp ~/openclaw-backup-2026-02-13.tar.gz /path/to/backup-repo/

# 提交到 GitHub
cd /path/to/backup-repo
git add openclaw-backup-2026-02-13.tar.gz
git commit -m "Add OpenClaw backup (192MB)"
git push
```

## 6. 最佳实践
- 定期执行备份（建议每周一次）
- 测试备份文件的完整性
- 保留多个历史备份版本
- 注意 GitHub 单文件 100MB 限制，此备份需使用 LFS