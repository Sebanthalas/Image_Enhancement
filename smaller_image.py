"""
Example code for testing.
Author: Sebastian Moraga Scheuermann
Date: October 22, 2024.
Description:   script that lowers the resolution of the images for testing.
"""

import cv2
import glob
import argparse
import os

# Argument parsing
parser = argparse.ArgumentParser()
parser.add_argument("--video_name",    default = 'video',   type = str, help = "video name")
parser.add_argument("--resize_factor", default = 50,        type = int, help = "resize percentage (e.g., 50 for 50%)")
parser.add_argument("--input_dir",     default = None,      type = str, help = "input directory for images")
parser.add_argument("--output_dir",    default = None,      type = str, help = "output directory for resized images")

args = parser.parse_args()

# Set input and output directories
video_name  = args.video_name
input_dir   = args.input_dir  if args.input_dir  else f'extracted_frames_{video_name}'
output_dir  = args.output_dir if args.output_dir else f'extracted_frames_{video_name}_LR'

# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Resize factor
resize_factor = args.resize_factor / 100.0

# Process each image in input_dir
for img_path in glob.glob(f'{input_dir}/*.jpg'):
    img = cv2.imread(img_path)
    if img is None:
        print(f"Error reading image {img_path}")
        continue
    
    # Calculate new dimensions
    new_width  = int(img.shape[1] * resize_factor)
    new_height = int(img.shape[0] * resize_factor)
    
    # Resize the image
    small_img = cv2.resize(img, (new_width, new_height))
    
    # Generate output path
    img_name        = os.path.basename(img_path)
    output_img_path = os.path.join(output_dir, img_name)
    
    # Save resized image
    cv2.imwrite(output_img_path, small_img)

    #print(f"Resized and saved image to {output_img_path}")