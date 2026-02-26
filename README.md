# VPS 备份仓库

## 备份列表

### Clawdbot 5: github weixia994-gmail-com (AI 助手本体)
- **目录**: `clawdbot5-github/`
- **平台**: GitHub Codespaces
- **备份**: 44MB (2026-02-26)
- **内容**: OpenClaw 配置、技能、知识库、项目

### VPS1: Clawdbot 1 wujizhang hax us
- **目录**: `vps1-clawdbot1-us/`
- **IPv6**: `2602:294:0:dc:1234:4321:7f68:0001`
- **备份**: 445MB (2026-02-26)

### VPS2: RDP-us-clawdbot
- **目录**: `vps2-rdp-us/`
- **IPv6**: `2602:294:0:b7:1234:1234:dbca:0001`
- **备份**: 1.4GB (2026-02-26)

## 恢复指南

详细恢复步骤请查看：[RESTORE_GUIDE.md](RESTORE_GUIDE.md)

## 目录结构

```
.
├── README.md
├── RESTORE_GUIDE.md
├── clawdbot5-github/           # AI 助手本体备份
│   ├── README.md
│   └── clawdbot5-backup-2026-02-26.tar.gz (44MB)
├── vps1-clawdbot1-us/          # VPS1 备份
│   ├── README.md
│   └── vps-ipv6-backup-2026-02-26.tar.gz (445MB)
└── vps2-rdp-us/                # VPS2 备份
    ├── README.md
    └── vps2-ipv6-backup-2026-02-26.tar.gz (1.4GB)
```

## 添加新备份

```bash
# 复制到对应 VPS 目录
cp /tmp/new-backup.tar.gz vps1-clawdbot1-us/
# 或
cp /tmp/new-backup.tar.gz vps2-rdp-us/

# 提交到 Git
git add .
git commit -m "Add backup for YYYY-MM-DD"
git push origin main
```

---
*最后更新：2026-02-26*
