"""
Example code for testing.
Author: Sebastian Moraga Scheuermann
Date: October 22, 2024
Description:   script to create the gif from a folder containing the images.
"""

from PIL import Image
import glob
import argparse

# Parameters for GIF
parser = argparse.ArgumentParser()
parser.add_argument("--output_gif",        type = str, help = "output name") 
parser.add_argument("--image_folder",      type = str, help = "image folder") 
parser.add_argument("--_format",            type = str, help = "format") 
args = parser.parse_args()

output_gif = args.output_gif
image_folder = args.image_folder # Directory where the upscaled images are stored
_format = args._format
duration = 29  # Duration between frames in milliseconds (100 ms = 10 fps)
print(output_gif)
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
