#!/usr/bin/env python3
"""
Video Content Generator for Qiuzhi Video Maker Skill
Generates YouTube video scripts based on the analyzed data
"""

import pandas as pd
import random
import os
import re
from datetime import datetime

def load_crush_data(excel_path):
    """Load the crush data from Excel file"""
    df = pd.read_excel(excel_path)
    df_clean = df.dropna(how='all')
    return df_clean

def extract_clean_answer(answer_text):
    """Extract clean answer text without the number prefix"""
    if pd.isna(answer_text):
        return "No answer provided"
    # Remove leading numbers and periods (e.g., "1. ", "2. ", etc.)
    clean_text = re.sub(r'^\d+\.\s*', '', str(answer_text)).strip()
    return clean_text

def generate_video_script(topic, answers):
    """Generate a video script based on a topic and its answers"""
    script = f"""# Video Script: {topic}

## Hook (0-15 seconds)
Are you wondering about {topic.lower()}? Based on thousands of real cases, we've discovered the most effective approaches that actually work.

## Introduction (15-30 seconds)
Today we're breaking down {topic.lower()}, sharing evidence-based insights that can transform how you approach relationships.

## Main Content (30-180 seconds)
Let's dive into the 5 key points:

1. {answers[0]}
2. {answers[1]}
3. {answers[2]}
4. {answers[3]}
5. {answers[4]}

## Analysis of Each Point
- Point 1: This is often the most overlooked aspect, yet it's fundamental to success.
- Point 2: This builds on the first point and creates deeper connections.
- Point 3: This addresses a common misconception many people have.
- Point 4: This is where most people make mistakes, so pay close attention.
- Point 5: This ties everything together for lasting results.

## Practical Application (180-210 seconds)
Now, how can you apply these insights in your daily life?

## Conclusion (210-240 seconds)
Remember, {topic.lower()} requires patience and authenticity. The key is to implement these strategies gradually and genuinely.

## Call to Action (240-250 seconds)
Liked this video? Subscribe for more relationship insights based on real data analysis. Share your experiences in the comments below!
"""
    return script

def generate_video_metadata(topic, answers):
    """Generate title, description, and tags for a YouTube video"""
    title = f"{topic} - Based on 5000+ Real Cases"
    
    description = f"""{topic} - Based on 5000+ Real Cases

In this video, we analyze {topic.lower()} based on data from over 5000 real cases. Discover the 5 key insights that can transform your understanding of relationships.

🔍 What You'll Learn:
1. {answers[0]}
2. {answers[1]}
3. {answers[2]}
4. {answers[3]}
5. {answers[4]}

⏰ Timestamps:
0:00 Hook
0:15 Introduction
0:30 Main Content
3:00 Analysis
3:30 Practical Application
3:50 Conclusion
4:10 Call to Action

#RelationshipAdvice #DatingTips #{topic.replace(' ', '')} #{topic.split()[1] if len(topic.split()) > 1 else 'Love'}"""

    tags = [
        "relationship advice",
        "dating tips", 
        "love tips",
        "crush advice",
        "romance",
        topic.replace(" ", ""),
        "relationship psychology",
        "dating advice",
        "attraction",
        "communication"
    ]
    
    return title, description, tags

def create_batch_videos(excel_path, num_videos=10, output_dir="./output"):
    """Create a batch of video content based on the data"""
    df = load_crush_data(excel_path)
    
    # Get unique topics
    topics = df.dropna(how='all')['题目'].unique()
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate content for specified number of videos
    for i in range(min(num_videos, len(topics))):
        topic = topics[i]
        # Get the answers for this topic
        topic_row = df[df['题目'] == topic].iloc[0]
        
        answers = []
        for j in range(1, 6):  # Answers 1-5
            answer_col = f'答案{j}'
            if answer_col in df.columns and pd.notna(topic_row[answer_col]):
                # Extract clean answer without the number prefix
                clean_answer = extract_clean_answer(topic_row[answer_col])
                answers.append(clean_answer)
            else:
                answers.append(f"Answer {j} for {topic}")
        
        # Generate content
        script = generate_video_script(topic, answers)
        title, description, tags = generate_video_metadata(topic, answers)
        
        # Save content
        filename_base = f"video_{i+1:02d}_{topic.replace(' ', '_').replace(':', '').replace(',', '')}"
        
        # Save script
        with open(os.path.join(output_dir, f"{filename_base}_script.txt"), 'w', encoding='utf-8') as f:
            f.write(script)
        
        # Save metadata
        metadata = f"""Title: {title}
        
Description:
{description}

Tags: {', '.join(tags)}
"""
        with open(os.path.join(output_dir, f"{filename_base}_metadata.txt"), 'w', encoding='utf-8') as f:
            f.write(metadata)
        
        print(f"Generated content for: {topic}")

if __name__ == "__main__":
    # Example usage
    excel_path = '/workspaces/clawdbot/qiuzhi-project/qiuzhi-data-analyst/assets/男女事实.xlsx'
    
    if os.path.exists(excel_path):
        print("Generating batch of 10 video contents...")
        create_batch_videos(excel_path, num_videos=10, output_dir='./output')
        print("Batch generation complete!")
    else:
        print(f"Excel file not found at {excel_path}")
        print("Please ensure the data file exists.")