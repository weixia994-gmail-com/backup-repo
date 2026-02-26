#!/bin/bash
# 智能知识捕获脚本

DATE=$(date +%Y-%m-%d)
TIME=$(date +%H:%M:%S)
CATEGORY=${1:-inbox}

# 创建当日知识文件
KNOWLEDGE_FILE="/home/codespace/.openclaw/workspace/knowledge/$CATEGORY/${DATE}.md"

# 如果文件不存在，创建新文件
if [ ! -f "$KNOWLEDGE_FILE" ]; then
    echo "# $DATE 知识记录" > "$KNOWLEDGE_FILE"
    echo "" >> "$KNOWLEDGE_FILE"
    echo "## 当日要点" >> "$KNOWLEDGE_FILE"
    echo "" >> "$KNOWLEDGE_FILE"
fi

# 添加时间戳记录
echo "### $TIME" >> "$KNOWLEDGE_FILE"
echo "- $2" >> "$KNOWLEDGE_FILE"
echo "" >> "$KNOWLEDGE_FILE"

echo "知识已记录: $KNOWLEDGE_FILE"
