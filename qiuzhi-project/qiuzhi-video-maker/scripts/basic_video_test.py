#!/usr/bin/env python3
"""
Basic Video Renderer for Qiuzhi Video Maker
A simplified version to test video creation functionality
"""

import os
import re
from gtts import gTTS
from PIL import Image, ImageDraw

def create_basic_video_from_script(script_path, output_dir):
    """Create a very basic video from a script file"""
    print(f"Creating basic video from: {script_path}")
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Extract topic from filename
    topic = os.path.basename(script_path).replace('_script.txt', '')
    output_filename = f"{topic}_basic.mp4"
    output_path = os.path.join(output_dir, output_filename)
    
    # Read the script
    with open(script_path, 'r', encoding='utf-8') as f:
        script_content = f.read()
    
    # Clean the script for TTS
    clean_content = re.sub(r'#.*?\n', '', script_content)  # Remove headers
    clean_content = re.sub(r'\*.*?\*', '', clean_content)  # Remove formatting
    # Remove excessive text to avoid truncation mid-sentence
    clean_content = clean_content[:800]  # Increase limit and ensure complete sentences
    # Ensure we end at a sentence boundary if possible
    last_period = clean_content.rfind('.', 0, 800)
    if last_period > 0:
        clean_content = clean_content[:last_period+1]
    
    print("Creating audio with gTTS...")
    # Create a temporary audio file
    temp_audio_path = f"/tmp/{topic}_temp_audio.mp3"
    
    try:
        # Convert script to speech
        tts = gTTS(text=clean_content, lang='en', slow=False)
        tts.save(temp_audio_path)
        
        print("Audio created successfully!")
        print(f"Audio saved to: {temp_audio_path}")
        print("Note: Actual video rendering requires additional FFmpeg setup")
        print("The audio file contains the narrated script content")
        
        # Return the path to the audio file as a placeholder
        # In a full implementation, we would combine this with video
        return temp_audio_path
        
    except Exception as e:
        print(f"Error creating audio: {str(e)}")
        return None

if __name__ == "__main__":
    # Test with a single script file
    script_path = "/workspaces/clawdbot/qiuzhi-project/qiuzhi-video-maker/output/video_01_5_Subtle_Ways_to_Get_Your_Crush's_Attention_script.txt"
    output_dir = "/workspaces/clawdbot/qiuzhi-project/qiuzhi-video-maker/rendered_videos"
    
    if os.path.exists(script_path):
        result = create_basic_video_from_script(script_path, output_dir)
        if result:
            print(f"Success! Created: {result}")
            print("This is an audio file containing the narrated script.")
            print("For full video functionality, additional video rendering setup is needed.")
        else:
            print("Failed to create video/audio.")
    else:
        print(f"Script file not found: {script_path}")