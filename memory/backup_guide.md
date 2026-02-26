# OpenClaw 系统备份指南

## 1. 备份目的
- 定期备份 OpenClaw 系统配置和数据
- 防止意外数据丢失
- 便于系统迁移和恢复

## 2. 备份文件生成命令
```bash
# 生成备份文件的完整命令
tar -czf openclaw-backup-$(date +%Y-%m-%d).tar.gz -C /home/codespace/.openclaw .

# 或者更完整的系统备份（包含工作区）
tar -czf openclaw-backup-$(date +%Y-%m-%d).tar.gz \
    -C /home/codespace/.openclaw . \
    -C /home/codespace/.openclaw/workspace .

# 最简命令（仅备份核心配置）
cd /home/codespace && tar -czf openclaw-backup-$(date +%Y-%m-%d).tar.gz .openclaw
```

## 3. 备份内容
- `.openclaw` 目录下的所有配置文件
- 认证信息和令牌
- 工作空间数据
- 日志文件

## 4. 推送到远程仓库
```bash
# 生成备份
tar -czf openclaw-backup-$(date +%Y-%m-%d).tar.gz -C /home/codespace/.openclaw .

# 推送到备份仓库
git push https://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@github.com/weixia994-gmail-com/backup-repo.git main
```

## 5. 自动化脚本示例
```bash
#!/bin/bash
# backup-openclaw.sh

DATE=$(date +%Y-%m-%d)
BACKUP_NAME="openclaw-backup-$DATE.tar.gz"

echo "开始创建 OpenClaw 备份: $BACKUP_NAME"

# 创建备份
tar -czf $BACKUP_NAME -C /home/codespace/.openclaw .

# 检查备份是否成功
if [ $? -eq 0 ]; then
    echo "备份创建成功: $BACKUP_NAME"
    
    # 可选：推送至远程仓库
    # git push https://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@github.com/weixia994-gmail-com/backup-repo.git main
    
else
    echo "备份创建失败!"
    exit 1
fi
```

## 6. 恢复备份
```bash
# 解压备份（请谨慎操作，会覆盖现有配置）
tar -xzf openclaw-backup-YYYY-MM-DD.tar.gz -C /home/codespace/.openclaw
```

## 7. 最佳实践
- 定期执行备份（建议每周一次）
- 测试备份文件的完整性
- 在推送前检查令牌安全性
- 保留多个历史备份版本