# VPS2: RDP-us-clawdbot

## 信息
- **IPv6**: `2602:294:0:b7:1234:1234:dbca:0001`
- **SSH 端口**: 22
- **用户**: root
- **位置**: US

## 备份文件

| 文件名 | 大小 | 日期 |
|--------|------|------|
| vps2-ipv6-backup-2026-02-26.tar.gz | 1.4GB | 2026-02-26 |

## 恢复命令

```bash
sshpass -p 'This-is-1-dog' ssh \
  -o ProxyCommand='nc -x 127.0.0.1:1080 -X 5 %h %p' \
  root@2602:294:0:b7:1234:1234:dbca:0001 \
  "cat > /tmp/restore.tar.gz" < vps2-ipv6-backup-2026-02-26.tar.gz

sshpass -p 'This-is-1-dog' ssh \
  -o ProxyCommand='nc -x 127.0.0.1:1080 -X 5 %h %p' \
  root@2602:294:0:b7:1234:1234:dbca:0001 \
  "tar -xzf /tmp/restore.tar.gz -C / && rm /tmp/restore.tar.gz"
```
