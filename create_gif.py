"""
Example code for testing.
Author: Sebastian Moraga Scheuermann
Date: October 28, 2024
Description:   script to create a GIF for both HD and LR images
"""

from PIL import Image
import glob
import argparse
import os

# Parameters for GIF
parser = argparse.ArgumentParser()
parser.add_argument("--video_name",        default='video',type=str, help="video name")
parser.add_argument("--_quality",          default='LR',   type=str, help="output directory for resized images")
parser.add_argument("--input_dir",         default=None,   type=str, help="input directory for resized images")
parser.add_argument("--image_folder",                      type=str, help="image folder") 
parser.add_argument("--_format",                           type=str, help="image format (e.g., jpg, png)")
parser.add_argument("--duration",          default=29,    type=int, help="Duration between frames in milliseconds (100 ms = 10 fps)")

args = parser.parse_args()

video_name    = args.video_name
_quality      = args._quality
image_folder  = args.input_dir if args.input_dir else f'extracted_frames_{video_name}_{_quality}'
_format       = args._format
duration      = args.duration  # Duration between frames in milliseconds (100 ms = 10 fps)

# Set output directory and file name
output_dir    = f'GIF_{video_name}'       # Folder to save the GIF
output_gif    = f'{output_dir}/GIF_{video_name}_{_quality}.gif'  # Full path including folder and file name

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

print(f'Saving GIF to {output_gif}')

# Get a list of image file paths in the results folder
image_paths = sorted(glob.glob(f'{image_folder}/*.{_format}'))

# Load the images
frames = [Image.open(img) for img in image_paths]

# Resize frames (optional) for visualization
size = (600, 600)  # Example size, adjust as needed
frames = [frame.resize(size, Image.ANTIALIAS) for frame in frames]

# Save as GIF
frames[0].save(
    output_gif, 
    format='GIF', 
    append_images=frames[1:], 
    save_all=True, 
    duration=duration, 
    loop=0
)

print(f'GIF saved as {output_gif}')
