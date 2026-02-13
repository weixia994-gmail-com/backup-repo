#!/usr/bin/env python3
"""
Detailed Audio Renderer for Qiuzhi Video Maker
Creates more detailed audio from script focusing on complete content
"""

import os
import re
from gtts import gTTS

def create_detailed_audio_from_script(script_path, output_dir):
    """Create detailed audio from a script file with complete content"""
    print(f"Creating detailed audio from: {script_path}")
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Extract topic from filename
    topic = os.path.basename(script_path).replace('_script.txt', '')
    output_filename = f"{topic}_detailed_audio.mp3"
    output_path = os.path.join(output_dir, output_filename)
    
    # Read the script
    with open(script_path, 'r', encoding='utf-8') as f:
        script_content = f.read()
    
    # Extract and structure the content to ensure completeness
    sections = {}
    
    # Split the script into sections
    parts = re.split(r'##\s+', script_content)
    
    for part in parts:
        if part.strip():
            lines = part.strip().split('\n', 1)
            if len(lines) > 1:
                section_title = lines[0].strip()
                section_content = lines[1].strip()
                sections[section_title] = section_content
    
    # Construct audio content with better flow and completeness
    audio_parts = []
    
    # Add hook if available
    if 'Hook (0-15 seconds)' in sections:
        hook_content = re.sub(r'\([^)]*\)', '', sections['Hook (0-15 seconds)']).strip()
        audio_parts.append(f"Hook. {hook_content}")
    
    # Add introduction
    if 'Introduction (15-30 seconds)' in sections:
        intro_content = re.sub(r'\([^)]*\)', '', sections['Introduction (15-30 seconds)']).strip()
        audio_parts.append(f"Introduction. {intro_content}")
    
    # Add main content with special attention to detail
    if 'Main Content (30-180 seconds)' in sections:
        main_content = sections['Main Content (30-180 seconds)']
        # Extract the 5 key points
        points = re.findall(r'\d+\.\s*(.*?)(?=\n\d+\.|$)', main_content, re.DOTALL)
        point_texts = []
        for i, point in enumerate(points, 1):
            point_text = point.strip()
            if point_text:
                point_texts.append(f"Number {i}. {point_text}")
        
        if point_texts:
            audio_parts.append(f"Main content. Here are the {len(point_texts)} key points.")
            audio_parts.extend(point_texts)
    
    # Add analysis of each point with more detail
    if 'Analysis of Each Point' in sections:
        analysis_content = sections['Analysis of Each Point']
        # Extract analysis points
        analysis_points = re.findall(r'-\s*Point\s+(\d+):\s*(.*?)(?=-\s*Point\s+\d+:|$)', analysis_content, re.DOTALL)
        analysis_texts = []
        for num, analysis in analysis_points:
            analysis_text = analysis.strip()
            if analysis_text:
                analysis_texts.append(f"Analysis of point {num}. {analysis_text}")
        
        if analysis_texts:
            audio_parts.append("Now for the analysis of each point.")
            audio_parts.extend(analysis_texts)
    
    # Add practical application
    if 'Practical Application (180-210 seconds)' in sections:
        prac_content = re.sub(r'\([^)]*\)', '', sections['Practical Application (180-210 seconds)']).strip()
        audio_parts.append(f"Practical application. {prac_content}")
    
    # Add conclusion
    if 'Conclusion (210-240 seconds)' in sections:
        concl_content = re.sub(r'\([^)]*\)', '', sections['Conclusion (210-240 seconds)']).strip()
        audio_parts.append(f"Conclusion. {concl_content}")
    
    # Add call to action
    if 'Call to Action (240-250 seconds)' in sections:
        cta_content = re.sub(r'\([^)]*\)', '', sections['Call to Action (240-250 seconds)']).strip()
        audio_parts.append(f"Call to action. {cta_content}")
    
    # Join all parts
    audio_content = ". ".join(audio_parts) + "."
    
    print(f"Creating detailed audio with {len(audio_content)} characters of content...")
    print(f"Content preview: {audio_content[:300]}...")
    
    try:
        # Convert script to speech with emphasis on clarity
        tts = gTTS(text=audio_content, lang='en', slow=False)
        tts.save(output_path)
        
        print("Detailed audio created successfully!")
        print(f"Audio saved to: {output_path}")
        
        return output_path
        
    except Exception as e:
        print(f"Error creating detailed audio: {str(e)}")
        return None

if __name__ == "__main__":
    # Test with a single script file
    script_path = "/workspaces/clawdbot/qiuzhi-project/qiuzhi-video-maker/output/video_01_5_Subtle_Ways_to_Get_Your_Crush's_Attention_script.txt"
    output_dir = "/home/codespace/.openclaw/media/outbound"
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    if os.path.exists(script_path):
        result = create_detailed_audio_from_script(script_path, output_dir)
        if result:
            print(f"Success! Created: {result}")
            print("This audio file contains the detailed and complete script content.")
        else:
            print("Failed to create detailed audio.")
    else:
        print(f"Script file not found: {script_path}")