#!/usr/bin/env python3
"""
Video Renderer for Qiuzhi Video Maker
Converts text scripts to actual video files
"""

import os
import subprocess
from pathlib import Path
from gtts import gTTS
from pydub import AudioSegment
from moviepy.editor import *
import re

def text_to_speech(text, output_path, lang='en'):
    """Convert text to speech audio file"""
    # Clean text to remove markdown formatting
    clean_text = re.sub(r'#+\s*', '', text)  # Remove headers
    clean_text = re.sub(r'\*.*?\*', '', clean_text)  # Remove bold/italic
    clean_text = re.sub(r'-\s*', '', clean_text)  # Remove list markers
    
    tts = gTTS(text=clean_text, lang=lang, slow=False)
    tts.save(output_path)

def create_background_music(duration_ms, output_path):
    """Create a simple background music track"""
    # For now, we'll create silence with a soft fade-in/out
    # In production, we would use actual background music
    silence = AudioSegment.silent(duration=duration_ms)
    # Apply gentle fade in/out
    faded_audio = silence.fade_in(2000).fade_out(2000)
    faded_audio.export(output_path, format="mp3")

def combine_audio_files(narration_path, bg_music_path, output_path, bg_volume=-20):
    """Combine narration with background music"""
    # Load audio files
    narration = AudioSegment.from_mp3(narration_path)
    bg_music = AudioSegment.from_mp3(bg_music_path)
    
    # Adjust background music volume
    bg_music = bg_music - abs(bg_volume)  # Reduce volume by 20dB
    
    # If background music is shorter than narration, loop it
    if len(bg_music) < len(narration):
        bg_music = bg_music * (len(narration) // len(bg_music) + 1)
    
    # Trim background music to match narration length
    bg_music = bg_music[:len(narration)]
    
    # Mix the audio
    mixed_audio = narration.overlay(bg_music)
    mixed_audio.export(output_path, format="mp3")

def create_video_with_audio(audio_path, output_video_path, duration=None):
    """Create a simple video with static image and audio"""
    # Create a temporary image for the video
    temp_image_path = "/tmp/temp_bg.jpg"
    
    # Create a simple image with text indicating the topic
    from PIL import Image, ImageDraw, ImageFont
    img = Image.new('RGB', (1280, 720), color=(30, 30, 60))  # Dark blue background
    d = ImageDraw.Draw(img)
    
    # Try to get the topic from the audio filename
    topic = os.path.basename(audio_path).replace('_audio.mp3', '').replace('_', ' ')
    
    # Add title text
    try:
        # Use default font or specify a font path
        d.text((100, 300), topic, fill=(255, 255, 255), align="center")
    except:
        # Fallback if font is not available
        d.text((100, 300), topic, fill=(255, 255, 255))
    
    img.save(temp_image_path)
    
    # Load the image as a video clip
    video_clip = ImageClip(temp_image_path, duration=AudioFileClip(audio_path).duration)
    
    # Add audio to the video
    audio_clip = AudioFileClip(audio_path)
    final_video = video_clip.set_audio(audio_clip)
    
    # Write the result
    final_video.write_videofile(
        output_video_path,
        fps=24,
        codec='libx264',
        audio_codec='aac',
        temp_audiofile='/tmp/temp-audio.m4a',
        remove_temp=True
    )
    
    # Clean up temp image
    os.remove(temp_image_path)

def render_video_from_script(script_path, output_dir):
    """Render a complete video from a script file"""
    print(f"Rendering video from: {script_path}")
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Extract topic from filename
    topic = os.path.basename(script_path).replace('_script.txt', '')
    output_prefix = os.path.join(output_dir, topic)
    
    # Define temporary paths
    narration_path = f"{output_prefix}_narration.mp3"
    bg_music_path = f"{output_prefix}_bg_music.mp3"
    combined_audio_path = f"{output_prefix}_audio.mp3"
    output_video_path = f"{output_prefix}_final.mp4"
    
    # Read the script
    with open(script_path, 'r', encoding='utf-8') as f:
        script_content = f.read()
    
    # Convert script to speech
    print("Converting script to speech...")
    text_to_speech(script_content, narration_path)
    
    # Create background music
    print("Creating background music...")
    # Estimate duration based on text length (roughly 150 words per minute)
    word_count = len(script_content.split())
    estimated_duration_ms = (word_count / 150) * 60 * 1000  # Convert to milliseconds
    create_background_music(int(estimated_duration_ms), bg_music_path)
    
    # Combine audio tracks
    print("Combining audio tracks...")
    combine_audio_files(narration_path, bg_music_path, combined_audio_path)
    
    # Create video with audio
    print("Creating final video...")
    create_video_with_audio(combined_audio_path, output_video_path)
    
    # Clean up temporary files
    for temp_file in [narration_path, bg_music_path, combined_audio_path]:
        if os.path.exists(temp_file):
            os.remove(temp_file)
    
    print(f"Video rendered successfully: {output_video_path}")
    return output_video_path

def batch_render_videos(scripts_dir, output_dir):
    """Render all scripts in the directory"""
    script_files = [f for f in os.listdir(scripts_dir) if f.endswith('_script.txt')]
    
    print(f"Found {len(script_files)} script files to render")
    
    for script_file in script_files:
        script_path = os.path.join(scripts_dir, script_file)
        try:
            render_video_from_script(script_path, output_dir)
        except Exception as e:
            print(f"Error rendering {script_file}: {str(e)}")
            continue

if __name__ == "__main__":
    # Example usage
    scripts_dir = "./output"
    output_dir = "./rendered_videos"
    
    print("Starting video rendering process...")
    batch_render_videos(scripts_dir, output_dir)
    print("Video rendering process completed!")