#!/usr/bin/env python3
"""
Improved Audio Renderer for Qiuzhi Video Maker
Creates audio from script with better text handling
"""

import os
import re
from gtts import gTTS
from PIL import Image, ImageDraw

def create_improved_audio_from_script(script_path, output_dir):
    """Create audio from a script file with improved text handling"""
    print(f"Creating improved audio from: {script_path}")
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Extract topic from filename
    topic = os.path.basename(script_path).replace('_script.txt', '')
    output_filename = f"{topic}_audio.mp3"
    output_path = os.path.join(output_dir, output_filename)
    
    # Read the script
    with open(script_path, 'r', encoding='utf-8') as f:
        script_content = f.read()
    
    # Clean the script for TTS with better preservation of content
    # Remove headers but preserve the main content
    clean_content = re.sub(r'#.*?\n', '', script_content)  # Remove headers
    clean_content = re.sub(r'##.*?\n', '', clean_content)  # Remove subheaders
    clean_content = re.sub(r'-\s*', '', clean_content)  # Remove list markers
    clean_content = re.sub(r'\*\*.*?\*\*', lambda m: m.group(0)[2:-2], clean_content)  # Remove bold
    clean_content = re.sub(r'\*.*?\*', lambda m: m.group(0)[1:-1], clean_content)  # Remove italic
    
    # Focus on the main content parts for audio
    # Extract the hook, introduction and main points
    lines = clean_content.split('\n')
    filtered_lines = []
    
    for line in lines:
        line = line.strip()
        if line and not line.startswith('#'):
            # Include lines that contain the key information
            if any(keyword in line.lower() for keyword in ['hook', 'introduction', 'key points', '1.', '2.', '3.', '4.', '5.', 'conclusion', 'call to action']):
                # Remove time indicators like (0-15 seconds)
                line = re.sub(r'\([^)]*\)', '', line).strip()
                if line:
                    filtered_lines.append(line)
    
    # Join the important content
    audio_content = ' '.join(filtered_lines)
    
    # Limit length but ensure complete sentences
    if len(audio_content) > 1000:
        # Find a good cutoff point at sentence boundary
        sentences = re.split(r'[.!?]+', audio_content[:1001])
        audio_content = '. '.join(sentences[:-1]) + '.'  # Join all but the last (partial) sentence
    
    print(f"Creating audio with {len(audio_content)} characters of content...")
    
    try:
        # Convert script to speech
        tts = gTTS(text=audio_content, lang='en', slow=False)
        tts.save(output_path)
        
        print("Audio created successfully!")
        print(f"Audio saved to: {output_path}")
        print(f"Audio content preview: {audio_content[:200]}...")
        
        return output_path
        
    except Exception as e:
        print(f"Error creating audio: {str(e)}")
        return None

if __name__ == "__main__":
    # Test with a single script file
    script_path = "/workspaces/clawdbot/qiuzhi-project/qiuzhi-video-maker/output/video_01_5_Subtle_Ways_to_Get_Your_Crush's_Attention_script.txt"
    output_dir = "/home/codespace/.openclaw/media/outbound"
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    if os.path.exists(script_path):
        result = create_improved_audio_from_script(script_path, output_dir)
        if result:
            print(f"Success! Created: {result}")
            print("This audio file contains the cleaned and optimized script content.")
        else:
            print("Failed to create audio.")
    else:
        print(f"Script file not found: {script_path}")