#!/usr/bin/env python3
"""
Video Editor for Qiuzhi Video Maker
Handles video editing, background music integration and rendering
"""

import os
import subprocess
from pathlib import Path
from moviepy import VideoFileClip, AudioFileClip, ImageClip
from moviepy.audio import AudioFileClip
from moviepy.audio.io import AudioFileClip
from moviepy.video.io import VideoFileClip
from moviepy.audio.AudioClip import CompositeAudioClip
from moviepy.audio.fx.all import volumex
from moviepy.video.VideoClip import ImageClip
from moviepy.video.compositing import CompositeVideoClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.audio.compositing import CompositeAudioClip
from moviepy.tools import concatenate_audioclips, concatenate_videoclips
from moviepy.video.tools import concatenate_videoclips
from moviepy.audio.tools import concatenate_audioclips
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import random

class VideoEditor:
    def __init__(self, width=1280, height=720, fps=24):
        self.width = width
        self.height = height
        self.fps = fps
    
    def create_background_track(self, duration, bg_type="ambient", output_path="/tmp/bg_music.mp3"):
        """Create a background music track"""
        # For now, create a simple ambient sound using sine waves
        # In a real implementation, we would use actual music files
        
        # Create a simple tone as placeholder
        # This is a basic implementation - in practice, we'd use actual background music
        from scipy.io.wavfile import write
        import numpy as np
        
        # Generate a simple ambient tone
        sample_rate = 44100
        t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
        
        # Create a pleasant ambient sound
        frequency1 = 220  # Lower frequency
        frequency2 = 440  # Higher frequency
        wave = 0.3 * np.sin(2 * np.pi * frequency1 * t) + 0.2 * np.sin(2 * np.pi * frequency2 * t)
        
        # Apply a gentle envelope to fade in/out
        fade_samples = int(0.5 * sample_rate)  # 0.5 second fade
        fade_in = np.linspace(0, 1, fade_samples)
        fade_out = np.linspace(1, 0, fade_samples)
        
        if len(wave) > 2 * fade_samples:
            wave[:fade_samples] *= fade_in
            wave[-fade_samples:] *= fade_out
        else:
            mid_point = len(wave) // 2
            if mid_point > 0:
                wave[:mid_point] *= np.linspace(0, 1, mid_point)
                wave[mid_point:] *= np.linspace(1, 0, len(wave) - mid_point)
        
        # Normalize to prevent clipping
        wave = wave / np.max(np.abs(wave)) * 0.3  # Reduce volume to 30%
        
        write(output_path, sample_rate, (wave * 32767).astype(np.int16))
        return output_path
    
    def add_background_music(self, video_path, audio_path, bg_music_path, output_path, bg_volume=-20):
        """Add background music to video with narration"""
        # Load the video with narration
        video = VideoFileClip(video_path)
        narration_audio = video.audio
        
        # Load background music
        bg_music = AudioFileClip(bg_music_path)
        
        # Loop background music to match video length
        if bg_music.duration < video.duration:
            loops_needed = int(video.duration // bg_music.duration) + 1
            bg_music = concatenate_audioclips([bg_music] * loops_needed)
        
        # Trim to video length
        bg_music = bg_music.subclip(0, video.duration)
        
        # Adjust volume
        bg_music = bg_music.volumex(0.3)  # Reduce to 30% volume
        
        # Mix the narration with background music
        mixed_audio = CompositeAudioClip([narration_audio, bg_music])
        
        # Set the mixed audio to the video
        final_video = video.set_audio(mixed_audio)
        
        # Write the final video
        final_video.write_videofile(
            output_path,
            fps=self.fps,
            codec='libx264',
            audio_codec='aac',
            temp_audiofile='/tmp/temp-audio.m4a',
            remove_temp=True
        )
        
        # Close clips to free memory
        video.close()
        bg_music.close()
        final_video.close()
        
        return output_path
    
    def create_video_with_static_image_and_audio(self, audio_path, output_path, topic="Video Topic"):
        """Create a video with a static image and audio"""
        # Create a visually appealing background image
        img = Image.new('RGB', (self.width, self.height), color=self._get_random_color())
        draw = ImageDraw.Draw(img)
        
        # Add title text
        title = topic.replace('_', ' ').replace('video 0', 'Video ').replace(' 0', ' ')
        self._draw_centered_text(draw, title, (self.width//2, self.height//2), fontsize=48, fill=(255, 255, 255))
        
        # Add decorative elements
        self._add_decorative_elements(draw)
        
        # Save temporary image
        temp_img_path = "/tmp/temp_video_bg.png"
        img.save(temp_img_path)
        
        # Get audio duration
        audio_clip = AudioFileClip(audio_path)
        duration = audio_clip.duration
        
        # Create video clip from image
        video_clip = ImageClip(temp_img_path, duration=duration)
        
        # Add audio to video
        final_video = video_clip.set_audio(audio_clip)
        
        # Write the result
        final_video.write_videofile(
            output_path,
            fps=self.fps,
            codec='libx264',
            audio_codec='aac',
            temp_audiofile='/tmp/temp-audio.m4a',
            remove_temp=True
        )
        
        # Clean up
        os.remove(temp_img_path)
        audio_clip.close()
        final_video.close()
        
        return output_path
    
    def _get_random_color(self):
        """Generate a random pleasing color"""
        colors = [
            (70, 130, 180),   # Steel Blue
            (100, 149, 237),  # Cornflower Blue
            (65, 105, 225),   # Royal Blue
            (25, 25, 112),    # Midnight Blue
            (0, 191, 255),    # Deep Sky Blue
            (135, 206, 235),  # Sky Blue
            (135, 206, 250),  # Light Sky Blue
            (176, 224, 230),  # Powder Blue
            (173, 216, 230),  # Light Blue
        ]
        return random.choice(colors)
    
    def _draw_centered_text(self, draw, text, position, fontsize=48, fill=(255, 255, 255)):
        """Draw centered text on image"""
        try:
            # Try to use a better font if available
            from PIL import ImageFont
            font = ImageFont.truetype("arial.ttf", fontsize) if os.path.exists("arial.ttf") else ImageFont.load_default()
        except:
            font = ImageFont.load_default()
        
        # Calculate text size
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        # Calculate position for centering
        x = position[0] - text_width // 2
        y = position[1] - text_height // 2
        
        # Draw text with outline for better visibility
        self._draw_text_with_outline(draw, text, (x, y), font, fill)
    
    def _draw_text_with_outline(self, draw, text, position, font, fill, outline_fill=(0, 0, 0), outline_width=2):
        """Draw text with outline for better visibility"""
        x, y = position
        
        # Draw outline
        for dx in range(-outline_width, outline_width + 1):
            for dy in range(-outline_width, outline_width + 1):
                if dx != 0 or dy != 0:
                    draw.text((x + dx, y + dy), text, font=font, fill=outline_fill)
        
        # Draw main text
        draw.text((x, y), text, font=font, fill=fill)
    
    def _add_decorative_elements(self, draw):
        """Add decorative elements to the background"""
        import math
        
        # Add some subtle geometric patterns
        for i in range(5):
            x = random.randint(50, self.width-50)
            y = random.randint(50, self.height-50)
            radius = random.randint(20, 50)
            
            # Draw a semi-transparent circle
            draw.ellipse([x-radius, y-radius, x+radius, y+radius], 
                         outline=(255, 255, 255, 50), width=1)

def process_video_with_all_elements(script_path, output_dir):
    """Process a script to create a complete video with all elements"""
    print(f"Processing script: {script_path}")
    
    # Extract topic from filename
    topic = os.path.basename(script_path).replace('_script.txt', '')
    topic_clean = topic.replace('_', ' ').replace('video 0', 'Video ').replace(' 0', ' ')
    
    # Initialize video editor
    editor = VideoEditor()
    
    # Step 1: Create audio from script (using our existing TTS functionality)
    from gtts import gTTS
    import re
    
    with open(script_path, 'r', encoding='utf-8') as f:
        script_content = f.read()
    
    # Extract content for TTS (similar to our detailed audio renderer)
    sections = {}
    parts = re.split(r'##\s+', script_content)
    
    for part in parts:
        if part.strip():
            lines = part.strip().split('\n', 1)
            if len(lines) > 1:
                section_title = lines[0].strip()
                section_content = lines[1].strip()
                sections[section_title] = section_content
    
    # Construct audio content
    audio_parts = []
    
    if 'Hook (0-15 seconds)' in sections:
        hook_content = re.sub(r'\([^)]*\)', '', sections['Hook (0-15 seconds)']).strip()
        audio_parts.append(f"Hook. {hook_content}")
    
    if 'Introduction (15-30 seconds)' in sections:
        intro_content = re.sub(r'\([^)]*\)', '', sections['Introduction (15-30 seconds)']).strip()
        audio_parts.append(f"Introduction. {intro_content}")
    
    if 'Main Content (30-180 seconds)' in sections:
        main_content = sections['Main Content (30-180 seconds)']
        points = re.findall(r'\d+\.\s*(.*?)(?=\n\d+\.|$)', main_content, re.DOTALL)
        point_texts = []
        for i, point in enumerate(points, 1):
            point_text = point.strip()
            if point_text:
                point_texts.append(f"Number {i}. {point_text}")
        
        if point_texts:
            audio_parts.append(f"Main content. Here are the {len(point_texts)} key points.")
            audio_parts.extend(point_texts)
    
    if 'Analysis of Each Point' in sections:
        analysis_content = sections['Analysis of Each Point']
        analysis_points = re.findall(r'-\s*Point\s+(\d+):\s*(.*?)(?=-\s*Point\s+\d+:|$)', analysis_content, re.DOTALL)
        analysis_texts = []
        for num, analysis in analysis_points:
            analysis_text = analysis.strip()
            if analysis_text:
                analysis_texts.append(f"Analysis of point {num}. {analysis_text}")
        
        if analysis_texts:
            audio_parts.append("Now for the analysis of each point.")
            audio_parts.extend(analysis_texts)
    
    if 'Practical Application (180-210 seconds)' in sections:
        prac_content = re.sub(r'\([^)]*\)', '', sections['Practical Application (180-210 seconds)']).strip()
        audio_parts.append(f"Practical application. {prac_content}")
    
    if 'Conclusion (210-240 seconds)' in sections:
        concl_content = re.sub(r'\([^)]*\)', '', sections['Conclusion (210-240 seconds)']).strip()
        audio_parts.append(f"Conclusion. {concl_content}")
    
    if 'Call to Action (240-250 seconds)' in sections:
        cta_content = re.sub(r'\([^)]*\)', '', sections['Call to Action (240-250 seconds)']).strip()
        audio_parts.append(f"Call to action. {cta_content}")
    
    audio_content = ". ".join(audio_parts) + "."
    
    # Create narration audio
    temp_narration_path = f"/tmp/{topic}_narration.mp3"
    tts = gTTS(text=audio_content, lang='en', slow=False)
    tts.save(temp_narration_path)
    
    # Step 2: Create background music
    temp_bg_path = f"/tmp/{topic}_bg_music.mp3"
    editor.create_background_track(duration=AudioFileClip(temp_narration_path).duration, output_path=temp_bg_path)
    
    # Step 3: Create video with static image and narration
    temp_video_path = f"/tmp/{topic}_with_narration.mp4"
    editor.create_video_with_static_image_and_audio(temp_narration_path, temp_video_path, topic_clean)
    
    # Step 4: Add background music to the video
    final_output_path = os.path.join(output_dir, f"{topic}_final.mp4")
    editor.add_background_music(temp_video_path, temp_narration_path, temp_bg_path, final_output_path)
    
    # Cleanup temporary files
    for temp_file in [temp_narration_path, temp_bg_path, temp_video_path]:
        if os.path.exists(temp_file):
            os.remove(temp_file)
    
    print(f"Complete video created: {final_output_path}")
    return final_output_path

if __name__ == "__main__":
    print("Video Editor initialized. Ready to process scripts into complete videos with background music.")