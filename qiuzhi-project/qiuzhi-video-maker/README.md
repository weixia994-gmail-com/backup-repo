# Qiuzhi Video Maker

A specialized module for generating YouTube video content based on data insights.

## Features
- Generates video scripts from analyzed data
- Creates titles, descriptions, and tags
- Batch generates content (up to 10 per day as per YouTube limits)
- Uses templates for consistent formatting

## Structure
- `SKILL.md`: Skill definition for OpenClaw
- `scripts/video_content_generator.py`: Main content generation script
- `scripts/youtube_video_planner.sh`: Planning script
- `templates/`: Content templates
- `output/`: Generated content files

## Usage
```bash
python3 scripts/video_content_generator.py
```

This will generate 10 video scripts and metadata files based on the data insights.