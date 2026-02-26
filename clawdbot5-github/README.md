# Clawdbot 5: github weixia994-gmail-com

## 信息
- **名称**: Clawdbot 5
- **GitHub**: weixia994-gmail-com
- **平台**: GitHub Codespaces
- **身份**: AI 助手 (amy)
- **位置**: Cloud

## 备份文件

| 文件名 | 大小 | 日期 |
|--------|------|------|
| clawdbot5-backup-2026-02-26.tar.gz | 44MB | 2026-02-26 |

## 备份内容

- ✅ OpenClaw 配置 (`openclaw.json`)
- ✅ 身份文件 (SOUL.md, AGENTS.md, USER.md, IDENTITY.md, TOOLS.md)
- ✅ 记忆文件 (`memory/`)
- ✅ 知识库 (`knowledge/`)
- ✅ 技能 (`skills/`)
- ✅ 求职项目 (`qiuzhi-project/`)
- ✅ VPS 备份管理目录

## 恢复方法

### 本地恢复
```bash
# 解压备份
tar -xzf clawdbot5-backup-2026-02-26.tar.gz -C /path/to/restore/
```

### 恢复到新的 Codespace
```bash
# 1. 克隆仓库
git clone https://github.com/weixia994-gmail-com/backup-repo.git
cd backup-repo/clawdbot5-github

# 2. 解压备份
tar -xzf clawdbot5-backup-2026-02-26.tar.gz -C ~/

# 3. 恢复 OpenClaw 配置
cp ~/.openclaw/workspace/openclaw.json ~/.openclaw/

# 4. 重启 OpenClaw
openclaw gateway restart
```

### 完整恢复脚本
```bash
#!/bin/bash
BACKUP_FILE="$1"
TARGET_DIR="${2:-$HOME}"

echo "恢复 Clawdbot 5 到 $TARGET_DIR..."

# 解压
tar -xzf "$BACKUP_FILE" -C "$TARGET_DIR"

# 恢复配置
cp "$TARGET_DIR/.openclaw/workspace/openclaw.json" "$TARGET_DIR/.openclaw/"

# 重启服务
openclaw gateway restart

echo "恢复完成！"
```

## 身份配置

**IDENTITY.md:**
- **Name**: amy
- **Creature**: AI assistant
- **Vibe**: Professional, helpful, concise
- **Emoji**: 🤖

**模型配置:**
- 主模型：`qwen-portal/coder-model`
- 备用模型：`openai-codex/gpt-5.3-codex`

## 重要技能

- **smart-capture**: 智能内容捕获和摘要
- **telegram-handler**: Telegram 消息处理
- **video-frames**: 视频帧提取
- **weather**: 天气查询
- **github**: GitHub CLI 操作
- **healthcheck**: 系统健康检查

## 项目

- **qiuzhi-project**: 求职相关内容生成
  - 数据分析
  - 视频制作
  - 餐厅创意系统

## VPS 管理

Clawdbot 5 负责管理以下 VPS 备份：
- **VPS1**: Clawdbot 1 wujizhang hax us (445MB)
- **VPS2**: RDP-us-clawdbot (1.4GB)

## 日常任务

1. 每 5 分钟检查 Xray 状态
2. 处理 Telegram 消息
3. 管理 VPS 备份
4. 生成求职视频内容
5. 知识管理和整理

---
*最后备份：2026-02-26*
*备份大小：44MB*
