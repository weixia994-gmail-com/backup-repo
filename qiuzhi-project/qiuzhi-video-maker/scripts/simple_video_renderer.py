#!/usr/bin/env python3
"""
Simple Video Renderer for Qiuzhi Video Maker
Converts text scripts to actual video files with basic functionality
"""

import os
import re
from pathlib import Path
from gtts import gTTS

# Import from moviepy directly instead of moviepy.editor
from moviepy import ImageClip, AudioFileClip

def clean_script_for_tts(text):
    """Clean script text for text-to-speech conversion"""
    # Remove markdown headers and formatting
    text = re.sub(r'#+\s*', '', text)  # Remove headers
    text = re.sub(r'\*\*.*?\*\*', lambda m: m.group(0)[2:-2], text)  # Remove bold
    text = re.sub(r'\*.*?\*', lambda m: m.group(0)[1:-1], text)  # Remove italic
    text = re.sub(r'-\s*', '', text)  # Remove list markers
    text = re.sub(r'##.*?\n', '\n', text)  # Remove section headers
    text = re.sub(r'\n\s*\n', '\n', text)  # Remove excessive blank lines
    
    return text.strip()

def render_single_video(script_path, output_dir):
    """Render a single video from a script file"""
    print(f"Rendering video from: {script_path}")
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Extract topic from filename
    topic = os.path.basename(script_path).replace('_script.txt', '')
    output_filename = f"{topic}_final.mp4"
    output_path = os.path.join(output_dir, output_filename)
    
    # Read the script
    with open(script_path, 'r', encoding='utf-8') as f:
        script_content = f.read()
    
    # Clean the script for TTS
    clean_content = clean_script_for_tts(script_content)
    
    # Create a temporary audio file
    temp_audio_path = f"/tmp/{topic}_temp_audio.mp3"
    
    try:
        # Convert script to speech
        print("Converting script to speech...")
        tts = gTTS(text=clean_content, lang='en', slow=False)
        tts.save(temp_audio_path)
        
        # Create a simple video clip with a static image
        print("Creating video with audio...")
        
        # Create a simple image for the video background
        from PIL import Image, ImageDraw
        img = Image.new('RGB', (1280, 720), color=(70, 130, 180))  # Steel blue background
        draw = ImageDraw.Draw(img)
        
        # Add a title to the image
        title = topic.replace('_', ' ').replace('video 0', 'Video ').replace(' 0', ' ')
        draw.text((50, 300), title, fill=(255, 255, 255))
        
        # Save temporary image
        temp_img_path = "/tmp/temp_video_bg.jpg"
        img.save(temp_img_path)
        
        # Create video clip from image
        # Need to get the duration from the audio file
        audio_clip = AudioFileClip(temp_audio_path)
        video_duration = audio_clip.duration
        
        video_clip = ImageClip(temp_img_path, duration=video_duration)
        
        # Add audio to video
        final_video = video_clip.set_audio(audio_clip)
        
        # Write the final video
        final_video.write_videofile(
            output_path,
            fps=24,
            codec='libx264',
            audio_codec='aac'
        )
        
        # Clean up temporary files
        os.remove(temp_audio_path)
        os.remove(temp_img_path)
        
        print(f"Video rendered successfully: {output_path}")
        return output_path
        
    except Exception as e:
        print(f"Error rendering video: {str(e)}")
        # Clean up temp files if error occurs
        if os.path.exists(temp_audio_path):
            os.remove(temp_audio_path)
        if os.path.exists(temp_img_path):
            os.remove(temp_img_path)
        return None

def batch_render_videos(scripts_dir, output_dir):
    """Render all scripts in the directory"""
    script_files = [f for f in os.listdir(scripts_dir) if f.endswith('_script.txt')]
    
    print(f"Found {len(script_files)} script files to render")
    
    successful = 0
    for script_file in script_files[:2]:  # Limit to first 2 for testing
        script_path = os.path.join(scripts_dir, script_file)
        try:
            result = render_single_video(script_path, output_dir)
            if result:
                successful += 1
        except Exception as e:
            print(f"Error rendering {script_file}: {str(e)}")
            continue
    
    print(f"Video rendering process completed! {successful}/{len(script_files[:2])} videos rendered.")

if __name__ == "__main__":
    # Define directories
    scripts_dir = "/workspaces/clawdbot/qiuzhi-project/qiuzhi-video-maker/output"
    output_dir = "/workspaces/clawdbot/qiuzhi-project/qiuzhi-video-maker/rendered_videos"
    
    print("Starting video rendering process...")
    batch_render_videos(scripts_dir, output_dir)
    print("Check the rendered_videos folder for the final videos!")