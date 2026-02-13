#!/usr/bin/env python3
from PIL import Image, ImageEnhance
import os

def create_colored_favicon(input_path, output_path, hue_shift=0.3):
    """Create a new favicon with color modification"""
    
    # Open the original image
    img = Image.open(input_path)
    
    # Convert to RGBA if not already
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    # Create a copy for modification
    colored_img = img.copy()
    
    # Split into channels
    r, g, b, a = colored_img.split()
    
    # Convert to HSV for better color manipulation
    hsv_img = colored_img.convert('HSV')
    h, s, v = hsv_img.split()
    
    # Shift hue (change color while preserving brightness/saturation)
    h_data = list(h.getdata())
    h_shifted = [(int(pixel + hue_shift * 255) % 256) for pixel in h_data]
    h_new = Image.new('L', h.size)
    h_new.putdata(h_shifted)
    
    # Recombine HSV channels
    hsv_new = Image.merge('HSV', (h_new, s, v))
    
    # Convert back to RGBA
    rgb_new = hsv_new.convert('RGB')
    
    # Add back alpha channel
    colored_img = Image.merge('RGBA', (*rgb_new.split(), a))
    
    # Create multiple sizes for ICO format
    sizes = [(16, 16), (32, 32), (48, 48), (64, 64)]
    ico_images = []
    
    for size in sizes:
        resized = colored_img.resize(size, Image.Resampling.LANCZOS)
        ico_images.append(resized)
    
    # Save as ICO
    ico_images[0].save(output_path, format='ICO', sizes=[(img.width, img.height) for img in ico_images])
    print(f"Created {output_path} with color-shifted favicon")

if __name__ == "__main__":
    input_file = "./static/images/favicon.png"
    output_file = "./static/favicon1.ico"
    
    if os.path.exists(input_file):
        create_colored_favicon(input_file, output_file)
    else:
        print(f"Input file {input_file} not found")