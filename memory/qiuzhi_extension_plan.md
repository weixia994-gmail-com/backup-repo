# qiuzhi-project 扩展计划

## 当前项目结构
- qiuzhi-creative (创意技能)
- qiuzhi-restaurant (餐厅技能)

## 扩展方向

### 1. csv-data-summarizer
**功能**: 自动分析和汇总 CSV 数据
**实现**: 
- 创建 `qiuzhi-data-analyst` 模块
- 集成 pandas 和数据分析功能
- 生成可视化图表

### 2. file-organizer
**功能**: 自动整理文件系统
**实现**:
- 创建 `qiuzhi-file-organizer` 模块
- 智能分类和归档功能
- 支持自定义规则

### 3. video-downloader
**功能**: 视频下载和处理
**实现**:
- 增强现有的 YouTube 处理能力
- 集成 yt-dlp 功能
- 支持多种视频平台

### 4. research-skills
**功能**: 自动化研究功能
**实现**:
- 增强 `qiuzhi-creative` 的研究能力
- 集成 web_search 功能
- 自动生成研究报告

### 5. doc
**功能**: 文档处理
**实现**:
- 创建 `qiuzhi-doc-manager` 模块
- 支持多种文档格式
- 自动生成和编辑文档

### 6. Skill Creator
**功能**: 自动创建新技能
**实现**:
- 创建 `qiuzhi-skill-generator` 模块
- 模板化技能创建流程
- 自动化测试和部署

## 优先级
1. 增强 research-skills (提升第二大脑能力)
2. 完善 video-downloader (优化 YouTube 处理)
3. 添加 csv-data-summarizer (数据分析能力)
4. 开发 Skill Creator (自举能力)

## 集成方案
- 保持现有 qiuzhi-creative 和 qiuzhi-restaurant 模块
- 添加新的专用模块
- 确保与 OpenClaw 框架兼容