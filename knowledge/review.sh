#!/bin/bash
# 知识回顾脚本

DATE=$(date +%Y-%m-%d)
PREV_DATE=$(date -d "yesterday" +%Y-%m-%d)

echo "=== $DATE 知识回顾 ==="

# 显示今日新增知识
if [ -f "/home/codespace/.openclaw/workspace/knowledge/inbox/${DATE}.md" ]; then
    echo "今日新增知识:"
    cat "/home/codespace/.openclaw/workspace/knowledge/inbox/${DATE}.md"
    echo ""
fi

# 显示昨日知识回顾
if [ -f "/home/codespace/.openclaw/workspace/knowledge/inbox/${PREV_DATE}.md" ]; then
    echo "昨日知识回顾:"
    cat "/home/codespace/.openclaw/workspace/knowledge/inbox/${PREV_DATE}.md"
    echo ""
fi

# 统计本周知识量
THIS_WEEK=$(date +%Y-week%U)
WEEK_COUNT=$(find /home/codespace/.openclaw/workspace/knowledge/inbox -name "${DATE:0:4}-*-*.md" -newer "/home/codespace/.openclaw/workspace/knowledge/inbox/$(date -d '7 days ago' +%Y-%m-%d).md" 2>/dev/null | wc -l)
echo "本周已记录知识点: $WEEK_COUNT 个"
