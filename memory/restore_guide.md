# 新环境设置与备份恢复指南

## 1. 在新 GitHub 账户中设置

### 1.1 创建新的 Personal Access Token (PAT)
1. 登录到新的 GitHub 账户
2. 访问 Settings > Developer settings > Personal access tokens > Tokens (classic)
3. 点击 "Generate new token"
4. 选择适当的权限（至少包括 repo 和 read:user）
5. 复制生成的 token（格式类似：ghp_xxx...）

### 1.2 记录新的仓库地址
- 新的备份仓库地址：`https://github.com/[NEW_USERNAME]/backup-repo.git`

## 2. 在新 Codespace 中设置

### 2.1 克隆备份仓库
```bash
# 使用新的 PAT 克隆备份仓库
git clone https://[NEW_PAT]@github.com/[NEW_USERNAME]/backup-repo.git
```

### 2.2 安装 OpenClaw
```bash
# 安装 Node.js（如果尚未安装）
# 然后安装 OpenClaw
npm install -g openclaw
```

### 2.3 恢复备份
```bash
# 进入备份文件所在目录
cd backup-repo

# 找到最新的备份文件
ls -la openclaw-backup-*.tar.gz

# 解压备份到正确位置
mkdir -p /home/codespace/.openclaw
tar -xzf openclaw-backup-[DATE].tar.gz -C /home/codespace/.openclaw

# 验证恢复的文件
ls -la /home/codespace/.openclaw
```

## 3. 配置 OpenClaw

### 3.1 启动 OpenClaw
```bash
# 启动 OpenClaw 服务
openclaw gateway start
```

### 3.2 验证配置
```bash
# 检查 OpenClaw 状态
openclaw status
```

## 4. 配置 Git 凭据
```bash
# 配置 Git 用户信息
git config --global user.name "[NEW_USERNAME]"
git config --global user.email "[EMAIL]"

# 如果需要，配置 Git 凭据助手
git config --global credential.helper store
```

## 5. 验证系统功能
```bash
# 测试基本命令
openclaw --help

# 检查模型连接
# (根据您的配置测试 Qwen 或 Gemini 模型)

# 测试 Xray 服务（如果需要）
# 检查 /home/codespace/xray_config.json 是否正确配置
```

## 6. 自动化脚本示例
```bash
#!/bin/bash
# restore-openclaw.sh

# 设置变量
NEW_PAT="YOUR_NEW_PAT_HERE"
NEW_USERNAME="YOUR_NEW_USERNAME_HERE"
BACKUP_FILE="openclaw-backup-latest.tar.gz"

echo "开始在新环境中恢复 OpenClaw..."

# 克隆备份仓库
git clone https://$NEW_PAT@github.com/$NEW_USERNAME/backup-repo.git
cd backup-repo

# 找到最新的备份文件
LATEST_BACKUP=$(ls -t openclaw-backup-*.tar.gz | head -1)
echo "找到最新的备份文件: $LATEST_BACKUP"

# 创建 .openclaw 目录并恢复备份
mkdir -p /home/codespace/.openclaw
tar -xzf $LATEST_BACKUP -C /home/codespace/.openclaw

echo "备份恢复完成！"

# 启动 OpenClaw
openclaw gateway start

echo "OpenClaw 服务已启动，设置完成！"
```

## 7. 注意事项
- 确保新账户有访问备份仓库的权限
- 检查 API 令牌（如 Gemini、Qwen）是否需要更新
- 验证所有自定义脚本和配置是否兼容
- 更新任何硬编码的路径或账户信息
- 测试所有关键功能（如 YouTube 自动摘要、Xray 代理等）