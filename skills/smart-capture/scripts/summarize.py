#!/usr/bin/env python3
import sys
import os
import json
import subprocess
import datetime
import re

# --- 配置 ---
KNOWLEDGE_BASE_DIR = os.path.expanduser("~/.openclaw/workspace/knowledge")
TEMP_DIR = "/tmp/smart_capture"

def ensure_dirs():
    if not os.path.exists(TEMP_DIR):
        os.makedirs(TEMP_DIR)
    for subdir in ["inbox", "tech", "business", "life"]:
        path = os.path.join(KNOWLEDGE_BASE_DIR, subdir)
        if not os.path.exists(path):
            os.makedirs(path)

def is_youtube_url(url):
    return "youtube.com" in url or "youtu.be" in url

def fetch_youtube_content(url):
    print(f"🎥 Detected YouTube URL: {url}")
    print("⏳ Fetching metadata and subtitles with yt-dlp...")
    
    # 1. Get Metadata
    yt_dlp_cmd = "/home/linuxbrew/.linuxbrew/bin/yt-dlp"
    if not os.path.exists(yt_dlp_cmd):
        yt_dlp_cmd = "yt-dlp" # Fallback if not found

    try:
        cmd = [
            yt_dlp_cmd,
            "--proxy", "socks5://127.0.0.1:1080",
            "--dump-json",
            "--skip-download",
            "--no-warnings",
            url
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        metadata = json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to get metadata: {e.stderr}")
        return None

    # 2. Get Subtitles (Auto-sub or manual)
    sub_text = ""
    try:
        # Try to get auto-subs in English or Chinese
        cmd_sub = [
            yt_dlp_cmd,
            "--proxy", "socks5://127.0.0.1:1080",
            "--write-auto-sub",
            "--sub-lang", "en,zh-Hant,zh-Hans",
            "--skip-download",
            "--output", f"{TEMP_DIR}/%(id)s",
            url
        ]
        subprocess.run(cmd_sub, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        # Read the vtt file
        vtt_file = f"{TEMP_DIR}/{metadata['id']}.en.vtt" # Default check
        # Check for other languages if English not found
        for lang in ["en", "zh-Hant", "zh-Hans"]:
            potential_file = f"{TEMP_DIR}/{metadata['id']}.{lang}.vtt"
            if os.path.exists(potential_file):
                vtt_file = potential_file
                break
        
        if os.path.exists(vtt_file):
            with open(vtt_file, 'r', encoding='utf-8') as f:
                # Simple cleanup of VTT timestamps
                lines = f.readlines()
                unique_lines = []
                for line in lines:
                    if '-->' not in line and line.strip() and line.strip() != 'WEBVTT':
                        clean_line = line.strip()
                        if not unique_lines or unique_lines[-1] != clean_line:
                            unique_lines.append(clean_line)
                sub_text = "\n".join(unique_lines[:1000]) # Limit for context
        else:
            sub_text = "(No subtitles found)"
            
    except Exception as e:
        print(f"⚠️ Warning: Could not fetch subtitles: {e}")

    return {
        "title": metadata.get('title', 'Untitled Video'),
        "url": url,
        "author": metadata.get('uploader', 'Unknown'),
        "description": metadata.get('description', ''),
        "content": sub_text,
        "type": "video"
    }

def fetch_web_content(url):
    print(f"🌐 Detected Web URL: {url}")
    # In a real scenario, we'd use 'web_fetch' tool logic here.
    # Since this script runs INSIDE the environment, we might need to rely on the agent calling web_fetch FIRST
    # or implement a simple curl/readability fetcher here.
    # For now, let's assume the agent passes the content or we use a simple placeholder.
    # In a perfect world, we'd use 'lynx' or similar if installed.
    return {
        "title": "Web Article",
        "url": url,
        "author": "Unknown",
        "description": "Web content",
        "content": f"Content from {url} (Content fetching to be implemented via agent tools)",
        "type": "article"
    }

def generate_note_content(data):
    today = datetime.date.today().isoformat()
    
    # Template
    template = f"""# {data['title']}

- **Source**: {data['url']}
- **Author**: {data['author']}
- **Date**: {today}
- **Type**: #{data['type']}
- **Status**: #inbox

## 📝 Executive Summary
(Waiting for AI Analysis...)

## 💡 Key Insights
- Insight 1
- Insight 2
- Insight 3

## ✅ Actionable Items
- [ ] Action 1

## 🔗 References
- [Original Link]({data['url']})

---
## Raw Context (Snippet)
{data['description'][:500]}...

{data['content'][:1000]}...
"""
    return template

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 summarize.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    ensure_dirs()

    if is_youtube_url(url):
        data = fetch_youtube_content(url)
    else:
        data = fetch_web_content(url)

    if not data:
        print("❌ Failed to fetch content.")
        sys.exit(1)

    # Generate Note
    note_content = generate_note_content(data)
    
    # Save File
    safe_title = "".join([c for c in data['title'] if c.isalnum() or c in (' ', '-', '_')]).strip()
    safe_title = safe_title.replace(" ", "_")[:50]
    filename = f"{datetime.date.today().isoformat()}-{safe_title}.md"
    filepath = os.path.join(KNOWLEDGE_BASE_DIR, "inbox", filename)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(note_content)

    print(f"✅ Note created at: {filepath}")
    print("👉 Now, please use your LLM capabilities to fill in the 'Summary', 'Insights', and 'Actions' sections of this file.")

if __name__ == "__main__":
    main()
