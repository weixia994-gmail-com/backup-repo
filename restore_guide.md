# OpenClaw 系统恢复指南

## 1. 恢复前准备
- 确保在新的 Codespace 或环境中已安装 OpenClaw
- 准备好相应的认证令牌和密钥

## 2. 下载备份文件
- 从 GitHub 仓库下载 openclaw-backup-YYYY-MM-DD.tar.gz 文件
- 文件大小约为 192MB

## 3. 恢复步骤

### 3.1 解压备份文件
```bash
# 将备份文件放置在用户主目录
cd ~
tar -xzvf openclaw-backup-2026-02-13.tar.gz
```

### 3.2 验证恢复的文件
```bash
# 检查 .openclaw 目录是否已恢复
ls -la ~/.openclaw

# 检查 /workspaces/clawdbot 目录是否已恢复
ls -la /workspaces/clawdbot
```

### 3.3 启动 OpenClaw
```bash
# 启动 OpenClaw 服务
openclaw gateway start
```

### 3.4 验证系统功能
```bash
# 检查 OpenClaw 状态
openclaw status

# 测试基本功能
openclaw --help
```

## 4. 配置调整
- 根据新环境调整必要的配置
- 验证 API 令牌（如 Gemini、Qwen）是否需要更新
- 检查 Xray 代理配置是否适用

## 5. 功能验证清单
- [ ] OpenClaw 服务正常启动
- [ ] AI 模型连接正常
- [ ] Xray 代理服务运行正常
- [ ] 自动化脚本功能正常
- [ ] 知识库系统正常工作
- [ ] Telegram 集成正常

## 6. 注意事项
- 恢复过程会覆盖现有配置，请谨慎操作
- 某些环境特定的配置可能需要重新调整
- 检查所有自定义脚本和配置是否兼容新环境