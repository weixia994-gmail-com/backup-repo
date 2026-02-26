# VPS 备份恢复指南

## 备份文件列表

| 文件名 | 大小 | VPS | IPv6 地址 | 备份日期 |
|--------|------|-----|-----------|----------|
| `vps-ipv6-backup-2026-02-26.tar.gz` | 445MB | VPS1 | `2602:294:0:dc:1234:4321:7f68:0001` | 2026-02-26 |
| `vps2-ipv6-backup-2026-02-26.tar.gz` | 1.4GB | VPS2 | `2602:294:0:b7:1234:1234:dbca:0001` | 2026-02-26 |

## 恢复前准备

### 1. 下载备份文件

```bash
# 克隆仓库
git clone https://github.com/weixia994-gmail-com/backup-repo.git
cd backup-repo

# 或使用 Git LFS 拉取大文件
git lfs pull
```

### 2. 准备目标 VPS

确保目标 VPS：
- 可以访问 IPv6 网络
- 有足够的磁盘空间
- SSH 服务正常运行
- 已安装必要工具（tar, sshpass, netcat）

```bash
# 安装必要工具
apt-get update && apt-get install -y sshpass netcat-openbsd
```

## 恢复方法

### 方法一：本地解压恢复（推荐）

适用于有本地访问权限的情况：

```bash
# 解压备份文件
cd /tmp
tar -xzf /path/to/vps-ipv6-backup-2026-02-26.tar.gz -C /

# 或指定恢复到特定目录
mkdir -p /tmp/restore
tar -xzf /path/to/vps-ipv6-backup-2026-02-26.tar.gz -C /tmp/restore
```

### 方法二：通过 SSH 远程恢复

适用于远程 VPS 恢复：

```bash
# VPS1 恢复命令
sshpass -p 'VPS1_PASSWORD' ssh -o StrictHostKeyChecking=no root@VPS1_IPv4_or_IPv6 \
  "cat > /tmp/restore.tar.gz" < /path/to/vps-ipv6-backup-2026-02-26.tar.gz

sshpass -p 'VPS1_PASSWORD' ssh root@VPS1_IPv4_or_IPv6 \
  "tar -xzf /tmp/restore.tar.gz -C / && rm /tmp/restore.tar.gz"

# VPS2 恢复命令
sshpass -p 'VPS2_PASSWORD' ssh -o StrictHostKeyChecking=no root@VPS2_IPv4_or_IPv6 \
  "cat > /tmp/restore.tar.gz" < /path/to/vps2-ipv6-backup-2026-02-26.tar.gz

sshpass -p 'VPS2_PASSWORD' ssh root@VPS2_IPv4_or_IPv6 \
  "tar -xzf /tmp/restore.tar.gz -C / && rm /tmp/restore.tar.gz"
```

### 方法三：通过 IPv6 + SOCKS5 代理恢复

如果只能通过 IPv6 访问（使用 Xray 代理）：

```bash
# 确保 Xray 运行中
systemctl start xray  # 或你的启动方式

# VPS1 恢复
sshpass -p 'Xw10086@' ssh \
  -o StrictHostKeyChecking=no \
  -o ProxyCommand='nc -x 127.0.0.1:1080 -X 5 %h %p' \
  root@2602:294:0:dc:1234:4321:7f68:0001 \
  "cat > /tmp/restore.tar.gz" < /path/to/vps-ipv6-backup-2026-02-26.tar.gz

sshpass -p 'Xw10086@' ssh \
  -o StrictHostKeyChecking=no \
  -o ProxyCommand='nc -x 127.0.0.1:1080 -X 5 %h %p' \
  root@2602:294:0:dc:1234:4321:7f68:0001 \
  "tar -xzf /tmp/restore.tar.gz -C / && rm /tmp/restore.tar.gz"

# VPS2 恢复
sshpass -p 'This-is-1-dog' ssh \
  -o StrictHostKeyChecking=no \
  -o ProxyCommand='nc -x 127.0.0.1:1080 -X 5 %h %p' \
  root@2602:294:0:b7:1234:1234:dbca:0001 \
  "cat > /tmp/restore.tar.gz" < /path/to/vps2-ipv6-backup-2026-02-26.tar.gz

sshpass -p 'This-is-1-dog' ssh \
  -o StrictHostKeyChecking=no \
  -o ProxyCommand='nc -x 127.0.0.1:1080 -X 5 %h %p' \
  root@2602:294:0:b7:1234:1234:dbca:0001 \
  "tar -xzf /tmp/restore.tar.gz -C / && rm /tmp/restore.tar.gz"
```

## 恢复后验证

```bash
# 检查系统信息
uname -a
cat /etc/os-release

# 检查关键服务
systemctl status sshd
systemctl status xray  # 或其他关键服务

# 检查用户数据
ls -la /home/
ls -la /root/

# 检查网络配置
ip -6 addr show
ip -4 addr show

# 检查磁盘空间
df -h
```

## 注意事项

### ⚠️ 恢复前
1. **备份当前状态** - 恢复前建议先备份当前系统状态
2. **停止关键服务** - 恢复前停止数据库、Web 服务等
3. **检查磁盘空间** - 确保目标系统有足够空间

### ⚠️ 恢复后
1. **更新密码** - 恢复后建议修改所有密码
2. **更新 SSH 密钥** - 如果使用 SSH 密钥认证
3. **检查服务状态** - 确保所有服务正常启动
4. **更新网络配置** - 如果 IP 地址变化，更新网络配置

### ⚠️ 排除的目录
备份时已排除以下目录，恢复时不会包含：
- `/proc` - 进程信息
- `/sys` - 系统信息
- `/dev` - 设备文件
- `/tmp` - 临时文件
- `/run` - 运行时数据
- `/mnt` - 挂载点
- `/media` - 可移动媒体
- `/lost+found` - 文件系统恢复目录

## 快速恢复脚本

```bash
#!/bin/bash
# 快速恢复脚本 - restore_vps.sh

BACKUP_FILE="$1"
VPS_IP="$2"
VPS_PASS="$3"

if [ -z "$BACKUP_FILE" ] || [ -z "$VPS_IP" ] || [ -z "$VPS_PASS" ]; then
    echo "用法：$0 <备份文件> <VPS IP> <VPS 密码>"
    exit 1
fi

echo "开始恢复 $BACKUP_FILE 到 $VPS_IP..."

# 传输备份文件
sshpass -p "$VPS_PASS" ssh \
  -o StrictHostKeyChecking=no \
  -o ProxyCommand='nc -x 127.0.0.1:1080 -X 5 %h %p' \
  root@"$VPS_IP" \
  "cat > /tmp/restore.tar.gz" < "$BACKUP_FILE"

# 解压恢复
sshpass -p "$VPS_PASS" ssh \
  -o StrictHostKeyChecking=no \
  -o ProxyCommand='nc -x 127.0.0.1:1080 -X 5 %h %p' \
  root@"$VPS_IP" \
  "tar -xzf /tmp/restore.tar.gz -C / && rm /tmp/restore.tar.gz && echo '恢复完成！'"

echo "恢复完成！"
```

使用示例：
```bash
chmod +x restore_vps.sh
./restore_vps.sh vps-ipv6-backup-2026-02-26.tar.gz 2602:294:0:dc:1234:4321:7f68:0001 'Xw10086@'
./restore_vps.sh vps2-ipv6-backup-2026-02-26.tar.gz 2602:294:0:b7:1234:1234:dbca:0001 'This-is-1-dog'
```

## 故障排除

### 问题：无法连接到 IPv6 VPS
```bash
# 检查 Xray/代理状态
systemctl status xray

# 测试 SOCKS5 代理
curl --socks5 127.0.0.1:1080 https://www.google.com

# 测试 IPv6 连接
python3 -c "import socket; s=socket.socket(); s.connect(('127.0.0.1',1080)); print('代理正常')"
```

### 问题：恢复后服务无法启动
```bash
# 检查服务日志
journalctl -u sshd -n 50
journalctl -u xray -n 50

# 重新生成主机密钥
rm /etc/ssh/ssh_host_*
ssh-keygen -A
systemctl restart sshd
```

### 问题：网络配置错误
```bash
# 检查网络接口
ip addr show

# 临时修复网络
ip -6 addr add 2602:294:0:dc:1234:4321:7f68:0001/64 dev eth0
ip -6 route add default via 2602:294:0:dc::1
```

## 联系支持

如有问题，请提供：
1. VPS 编号（VPS1 或 VPS2）
2. 错误信息
3. 恢复方法
4. 系统日志

---
*最后更新：2026-02-26*
*备份工具：OpenClaw + Xray + SSH*
