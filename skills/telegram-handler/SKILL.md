# Telegram Handler

## Description
Processes incoming Telegram messages and routes them to appropriate workflows, especially for "Second Brain" capture. It detects hashtags and links.

## Usage
Use this skill when you receive a message from Telegram that:
- Contains a URL (e.g., "Summarize this: https://...")
- Contains a hashtag like `#idea`, `#todo`, `#summary`, `#read`.
- Is a forward from another channel.

## Triggers & Actions

### 1. Smart Capture / Summary
- **Trigger**: URL found in message OR user asks to "summarize", "read", "capture".
- **Action**: Call `smart-capture` skill (via `exec skills/smart-capture/scripts/summarize.py`).
- **Response**: Reply with "Reading..." then provide the structured note.

### 2. Quick Ideas
- **Trigger**: Hashtag `#idea` or `#thought`.
- **Action**: Append to `knowledge/inbox/ideas.md`.
- **Response**: Reply with "💡 Idea captured."

### 3. Todos
- **Trigger**: Hashtag `#todo`.
- **Action**: Append to `memory/YYYY-MM-DD.md` (daily log) AND `knowledge/inbox/todos.md`.
- **Response**: Reply with "✅ Added to task list."

## Example
User: "Check this out https://youtube.com/watch?v=..."
Assistant: (Recognizes URL -> Calls `smart-capture` -> Generates Summary Note)

User: "#idea We should build a new plugin for music."
Assistant: (Appends to `ideas.md` -> Confirms)
