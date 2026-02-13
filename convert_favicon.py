#!/usr/bin/env python3
from PIL import Image
import os

def convert_to_ico(input_path, output_path):
    """Convert PNG/SVG to ICO format"""
    
    # Open the image
    img = Image.open(input_path)
    
    # Convert to RGBA if needed
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    # Create multiple sizes for ICO format
    sizes = [(16, 16), (32, 32), (48, 48), (64, 64)]
    ico_images = []
    
    for size in sizes:
        resized = img.resize(size, Image.Resampling.LANCZOS)
        ico_images.append(resized)
    
    # Save as ICO
    ico_images[0].save(output_path, format='ICO', sizes=[(img.width, img.height) for img in ico_images])
    print(f"Converted {input_path} to {output_path}")

if __name__ == "__main__":
    # Try PNG first, then SVG
    input_files = ["./static/images/favicon.png", "./static/images/favicon.svg"]
    output_file = "./static/favicon1.ico"
    
    for input_file in input_files:
        if os.path.exists(input_file):
            convert_to_ico(input_file, output_file)
            break
    else:
        print("No input file found")