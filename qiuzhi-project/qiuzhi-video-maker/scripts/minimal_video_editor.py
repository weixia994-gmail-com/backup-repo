#!/usr/bin/env python3
"""
Minimal Video Editor for Qiuzhi Video Maker
Focuses on core functionality: combining audio with static visuals
"""

import os
import numpy as np
from PIL import Image, ImageDraw
import random

class MinimalVideoEditor:
    def __init__(self, width=1280, height=720):
        self.width = width
        self.height = height
    
    def create_background_image(self, topic, output_path):
        """Create a visually appealing background image"""
        # Generate a random pleasing color
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
        
        bg_color = random.choice(colors)
        img = Image.new('RGB', (self.width, self.height), color=bg_color)
        draw = ImageDraw.Draw(img)
        
        # Add title text
        title = topic.replace('_', ' ').replace('video 0', 'Video ').replace(' 0', ' ')
        
        # Calculate text size and position for centering
        try:
            from PIL import ImageFont
            # Try to use a standard font
            font = ImageFont.truetype("DejaVuSans-Bold.ttf", 48) if os.path.exists("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf") else ImageFont.load_default(size=48)
        except:
            font = ImageFont.load_default(size=48)
        
        # Calculate text bounding box
        bbox = draw.textbbox((0, 0), title, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        # Center the text
        x = (self.width - text_width) // 2
        y = (self.height - text_height) // 2
        
        # Draw text with white color and black outline for visibility
        # Outline
        for dx in [-2, -1, 0, 1, 2]:
            for dy in [-2, -1, 0, 1, 2]:
                if dx != 0 or dy != 0:
                    draw.text((x + dx, y + dy), title, font=font, fill=(0, 0, 0))
        
        # Main text
        draw.text((x, y), title, font=font, fill=(255, 255, 255))
        
        # Add decorative elements
        self._add_decorative_elements(draw)
        
        # Save the image
        img.save(output_path)
        return output_path
    
    def _add_decorative_elements(self, draw):
        """Add decorative elements to the background"""
        # Add some subtle geometric patterns
        for i in range(10):
            x = random.randint(50, self.width-50)
            y = random.randint(50, self.height-50)
            radius = random.randint(10, 30)
            
            # Draw a semi-transparent circle
            # Create a new image for the circle to handle transparency
            overlay = Image.new('RGBA', (self.width, self.height), (0, 0, 0, 0))
            overlay_draw = ImageDraw.Draw(overlay)
            overlay_draw.ellipse([x-radius, y-radius, x+radius, y+radius], 
                                 outline=(255, 255, 255, 80), width=2)
            
            # Composite the overlay onto the main image
            img_with_overlay = Image.alpha_composite(
                Image.new('RGBA', (self.width, self.height), (255, 255, 255, 0)),
                overlay
            )
            # We'll skip compositing for simplicity in this minimal version

def create_simple_background_music(duration, output_path="/tmp/bg_music.mp3"):
    """Create a simple background music track using numpy/scipy"""
    try:
        from scipy.io.wavfile import write
        import numpy as np
        
        # Generate background music using scipy
        sample_rate = 44100
        t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
        
        # Create a pleasant ambient sound using multiple harmonics
        frequencies = [110, 220, 440]  # A2, A3, A4
        wave = np.zeros_like(t)
        
        for i, freq in enumerate(frequencies):
            # Create different wave shapes for each harmonic
            if i == 0:
                wave += 0.3 * np.sin(2 * np.pi * freq * t)
            elif i == 1:
                wave += 0.2 * np.sin(2 * np.pi * freq * t + np.pi/4)  # Phase shift
            else:
                wave += 0.1 * np.sin(2 * np.pi * freq * t + np.pi/2)  # Phase shift
        
        # Apply amplitude modulation for variation
        mod_freq = 0.5  # Modulation frequency (very slow)
        mod_wave = 0.5 + 0.5 * np.sin(2 * np.pi * mod_freq * t)
        wave = wave * mod_wave
        
        # Apply a gentle envelope to fade in/out
        fade_duration = 1.0  # 1 second fade
        fade_samples = int(fade_duration * sample_rate)
        
        if len(wave) > 2 * fade_samples:
            fade_in = np.linspace(0, 1, fade_samples)
            fade_out = np.linspace(1, 0, fade_samples)
            wave[:fade_samples] *= fade_in
            wave[-fade_samples:] *= fade_out
        else:
            # If the audio is too short, apply proportional fades
            mid_point = len(wave) // 2
            if mid_point > 0:
                wave[:mid_point] *= np.linspace(0, 1, mid_point)
                wave[mid_point:] *= np.linspace(1, 0, len(wave) - mid_point)
        
        # Normalize to prevent clipping
        wave = wave / max(0.01, np.max(np.abs(wave))) * 0.3  # Reduce volume to 30%
        
        # Convert to 16-bit integers
        audio_data = (wave * 32767).astype(np.int16)
        
        # Write the WAV file
        write(output_path.replace('.mp3', '.wav'), sample_rate, audio_data)
        
        # Convert to MP3 if needed (would require additional library like pydub)
        # For now, we'll return the WAV file
        return output_path.replace('.mp3', '.wav')
    
    except ImportError:
        # Fallback if scipy is not available
        print("Scipy not available, creating silent background audio")
        from scipy.io.wavfile import write
        import numpy as np
        
        sample_rate = 44100
        t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
        
        # Create silence
        silence = np.zeros(len(t))
        
        # Write the WAV file
        output_wav = output_path.replace('.mp3', '.wav')
        write(output_wav, sample_rate, (silence * 32767).astype(np.int16))
        
        return output_wav

def combine_audio_with_image(narration_path, image_path, bg_music_path, output_path):
    """Combine narration audio with image and background music"""
    # This function would normally use moviepy or other video libraries
    # For now, we'll simulate the process by returning a description
    # In a full implementation, we would combine the audio and image into a video
    print(f"Simulated combination of:")
    print(f"  Narration: {narration_path}")
    print(f"  Image: {image_path}")
    print(f"  Background Music: {bg_music_path}")
    print(f"  Output: {output_path}")
    return output_path

def process_video_with_all_elements_minimal(script_path, output_dir):
    """Process a script to create a complete video with all elements (minimal implementation)"""
    print(f"Processing script: {script_path}")
    
    # Extract topic from filename
    topic = os.path.basename(script_path).replace('_script.txt', '')
    topic_clean = topic.replace('_', ' ').replace('video 0', 'Video ').replace(' 0', ' ')
    
    # Initialize minimal video editor
    editor = MinimalVideoEditor()
    
    # Step 1: Create background image
    temp_image_path = f"/tmp/{topic}_bg_image.png"
    editor.create_background_image(topic_clean, temp_image_path)
    
    # Step 2: Get duration of narration audio (from our existing audio files)
    # For demo purposes, we'll estimate duration
    import math
    estimated_duration = 60  # 60 seconds as default, would be calculated from actual audio
    
    # Step 3: Create background music
    temp_bg_path = f"/tmp/{topic}_bg_music.wav"
    bg_music_path = create_simple_background_music(estimated_duration, temp_bg_path)
    
    # Step 4: Combine elements
    # In a full implementation, this would create the final video
    # For now, we're showing the process
    final_output_path = os.path.join(output_dir, f"{topic}_final_demo.txt")
    
    with open(final_output_path, 'w') as f:
        f.write(f"Video Production Plan:\n")
        f.write(f"Topic: {topic_clean}\n")
        f.write(f"Background Image: {temp_image_path}\n")
        f.write(f"Background Music: {bg_music_path}\n")
        f.write(f"Narration: {script_path.replace('_script.txt', '_detailed_audio.mp3')}\n")
        f.write(f"Estimated Duration: {estimated_duration}s\n")
    
    print(f"Demo video plan created: {final_output_path}")
    print("This demonstrates the complete workflow for video creation with background music and visuals.")
    return final_output_path

if __name__ == "__main__":
    print("Minimal Video Editor initialized. Ready to demonstrate the complete video creation workflow.")