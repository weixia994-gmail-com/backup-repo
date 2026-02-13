# Filemail 文件下载说明

## 问题
- Filemail 链接: https://www.filemail.com/d/gvajeoreschicaz
- 有效期: 仅 7 天
- 问题: 无法通过自动化工具下载，受反爬虫保护

## 解决方案
由于 Filemail 的安全措施，必须通过浏览器手动下载：

### 手动下载步骤
1. 打开浏览器访问: https://www.filemail.com/d/gvajeoreschicaz
2. 在页面上找到下载按钮
3. 点击下载 "openclaw-backup-2026-02-13.tar.gz" (约167MB)
4. 保存文件到本地计算机

### 上传到备份仓库
下载完成后，可通过以下方式上传到 GitHub:
```bash
# 将下载的文件复制到备份仓库
cp ~/Downloads/openclaw-backup-2026-02-13.tar.gz /path/to/backup-repo/

# 提交到 GitHub
cd /path/to/backup-repo
git add openclaw-backup-2026-02-13.tar.gz
git commit -m "Add official backup file from Filemail (167MB)"
git push
```

## 时间紧迫
请尽快手动下载此文件，因为 Filemail 链接将在 7 天内失效。