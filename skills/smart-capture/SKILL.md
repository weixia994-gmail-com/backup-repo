# Smart Capture (Second Brain)

## Description
Capture, analyze, and summarize content from URLs (YouTube, Articles, GitHub) or text input. Generates structured Markdown notes for a "Second Brain" knowledge base.

## Usage
Use this skill when the user wants to:
- Summarize a YouTube video (transcripts + metadata).
- Deep read and summarize an article or blog post.
- Convert a GitHub repo's README/structure into a learning note.
- "Save this" or "Note this" or "Add to second brain".

## Tools
- `web_fetch`: For articles and GitHub.
- `exec` (yt-dlp): For YouTube videos (subtitles/metadata).
- `write`: To save the note to `knowledge/`.

## Script
The main logic is handled by `scripts/summarize.py` (which we will create next).

## Workflow
1. **Identify Source**: Check if input is a URL (YouTube vs Web) or raw text.
2. **Extract Content**:
   - **YouTube**: Use `yt-dlp` to get metadata and subtitles.
   - **Web**: Use `web_fetch` to get markdown.
3. **Analyze**: Use LLM to summarize and structure the content.
4. **Save**: Write to `knowledge/<category>/YYYY-MM-DD-Title.md`.
