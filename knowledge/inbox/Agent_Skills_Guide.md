# Agent Skills 指南 (秋芝2046)

From: https://guide-app-lyart.vercel.app/

## 1. 安装 Antigravity

首先我们需要一个 AI 编程工具。推荐使用Antigravity，目前免费， (Cursor/Trae/VSCode也可以)。

**步骤：**
1. [下载Antigravity](https://antigravity.google/)
2. 安装（Windows一路点击**下一步**就可以了）
3. 打开Antigravity进入引导页面（同样点击下一步就可以）
4. 登录谷歌
5. 进入Antigravity安装中文插件
6. 将终端窗口放到屏幕右边（小Tips,可选）

---

## 2. 安装 Claude Code (AI 辅助)

我们可以让 AI 帮我们安装 Claude Code。

**步骤：**
1. 在 [Claude Code官方文档](https://code.claude.com/docs/zh-CN/overview) 中点击复制页面
2. 在Antigravity（或任意AI编程工具）对话框中粘贴内容
3. 并在末尾输入`帮我安装下Claude Code`然后点击发送

---

## 2.1 安装 Claude Code (手动)

如果 AI 安装失败，或者你更喜欢手动控制，请使用终端命令安装。

**注意：** Windows 安装后若提示找不到 `claude` 命令，通常是环境变量问题，可询问 AI 解决。

### 代码片段
**Windows:**
```powershell
irm https://claude.ai/install.ps1 | iex
```
**macOS:**
```bash
curl -fsSL https://claude.ai/install.sh | bash
```
---

## 3. 安装 CC-Switch

CC-Switch 是一个用于切换 Claude Code 供应商（如官方、GLM、DeepSeek）的工具。

**步骤：**
1. 下载CC-Switch：[CC-Switch下载](https://github.com/farion1231/cc-switch/releases/tag/v3.10.1)（滚动页面到底部下载）
2. 安装（Windows全程点下一步就行了）

---

## 4. 配置 CC-Switch

**关键步骤：**
1. **必须**先添加一个官方供应商（即使没账号），否则可能出错。
2. 添加第三方供应商（如 GLM），输入 API Key。
3. 点击“启用”你想要的供应商。
4. 回到 Antigravity 新建终端，输入 `claude` 回车。
5. 选择主题。

**如果出现登录提示，说明配置未生效，请回到 Switch 重新切换供应商。**

### 代码片段
**Windows:**
```powershell
claude
```
**macOS:**
```bash
claude
```
---

## 5. Agent Skills 结构

Agent Skills 的标准目录结构如下。理解这个结构有助于我们创建自己的 Skill。
 - **详细讲解请观看视频**

### 代码片段
**Windows:**
```powershell
qiuzhi-creative/
├── SKILL.md 
├── scripts/
├── references/
└── assets/
```
**macOS:**
```bash
qiuzhi-creative/
├── SKILL.md 
├── scripts/
├── references/
└── assets/
```
---

## 6. 创建自己的 Skill

使用 `qiuzhi-skill-creator` 来生成你的 Skill。

**步骤：**
1. [下载qiuzhi-skill-creator](https://coooo3v9ru1ar80o.public.blob.vercel-storage.com/qiuzhi-skill-creator.zip) 
2. 将 `qiuzhi-skill-creator` 解压到 `.claude\skills` 下。
3. 在 CC 中输入 `/qiuzhi` 选择 `qiuzhi-skill-creator`。
4. 描述你的需求，根据引导选择或输入。
5. 可以拖入参考图和[文档](https://coooo3v9ru1ar80o.public.blob.vercel-storage.com/nano_banana_pro_api.md)。
6. 等待生成并自动修复错误。

---

## 7. 更多资源

- 下面是我整理的一些 Agent Skills 合集网站和仓库，非常丰富。
- 我也给大家单独打包了几个常用的skill：[skills包](https://coooo3v9ru1ar80o.public.blob.vercel-storage.com/agent-skills%E5%8C%85.zip)

### 🌐 Agent Skills合集

- [SkillsMP](https://skillsmp.com/zh)：聚合GitHub上超过11万+开源技能。
- [Agent Skills](https://agent-skills.md/)：6000+好用的技能。
- [Skills.sh](https://skills.sh/)：适合快速发现热门技能，支持一键安装。
- [SkillStore](https://skillstore.io/zh-hans)：中文友好的技能商店，上架技能都是经过安全审查的。
- [Skills Directory](https://www.skillsdirectory.com/)：Reddit社区推荐的技能合集。
- [Agent Skills (Me)](https://agentskills.me/)：编辑精选出来的一些技能合集。

### 📦 Agent Skills仓库

- [Anthropics Skills](https://github.com/anthropics/skills)：Anthropic 官方技能仓库。
- [Vercel Agent Skills](https://github.com/vercel-labs/agent-skills)：Vercel 官方技能仓库。
- [Awesome Agent Skills](https://github.com/JackyST0/awesome-agent-skills)： 精选出的技能合集仓库。
- [Antfu Skills](https://github.com/antfu/skills)
- [Ultimate Agent Skills Collection](https://github.com/ZhanlinCui/Ultimate-Agent-Skills-Collection)

---

## 8. 记得点赞、收藏、关注！

如果觉得这个教程对你有帮助，请给我三连哦！

关注 **秋芝2046**，获取更多 AI 干货。

### 社交媒体
- [Bilibili](https://space.bilibili.com/385670211)
- [抖音](https://www.douyin.com/user/MS4wLjABAAAAwbbVuf1W2DdgRe0xCa0oxg1ZIHbzuiTzyjq3NcOVgBuu6qIidYlMYqbL3ZFY2swu)
- [小红书](https://www.xiaohongshu.com/user/profile/63b622ab00000000260066bd)
- [公众号](https://mp.weixin.qq.com/s/jCi9cVZYR1UqQ7xXOhn5iQ)
- [YouTube](https://www.youtube.com/@qiuzhi2046)

---

