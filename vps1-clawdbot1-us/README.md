# VPS1: Clawdbot 1 wujizhang hax us

## 信息
- **IPv6**: `2602:294:0:dc:1234:4321:7f68:0001`
- **SSH 端口**: 22
- **用户**: root
- **位置**: US

## 备份文件

| 文件名 | 大小 | 日期 |
|--------|------|------|
| vps-ipv6-backup-2026-02-26.tar.gz | 445MB | 2026-02-26 |

## 恢复命令

```bash
sshpass -p 'Xw10086@' ssh \
  -o ProxyCommand='nc -x 127.0.0.1:1080 -X 5 %h %p' \
  root@2602:294:0:dc:1234:4321:7f68:0001 \
  "cat > /tmp/restore.tar.gz" < vps-ipv6-backup-2026-02-26.tar.gz

sshpass -p 'Xw10086@' ssh \
  -o ProxyCommand='nc -x 127.0.0.1:1080 -X 5 %h %p' \
  root@2602:294:0:dc:1234:4321:7f68:0001 \
  "tar -xzf /tmp/restore.tar.gz -C / && rm /tmp/restore.tar.gz"
```
