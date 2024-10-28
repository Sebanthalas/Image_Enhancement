#!/bin/bash -vv

python --version
# Run parameters
# Choose the frames to extract

declare -r start_frame=1    # Starting of the video
declare -r end_frame=2      # Ending of the video
declare -r video_name="flowers"      # Ending of the video
declare -r resize_factor='50'      # Ending of the video
declare -r model_path='models/RRDB_ESRGAN_x4.pth'

echo "CONTROL: starting extract the frames from the video"
python3 extract.py --video_name $video_name --start_frame $start_frame --end_frame $end_frame 

echo "CONTROL: starting making the image even smaller"
python3 smaller_image.py --video_name $video_name --resize_factor $resize_factor

echo "CONTROL: starting to run ESRGAN model"
python3 ESRGAN/test.py --model_path $model_path --video_name $video_name

echo "CONTROL: starting to create the upscaled gif"
#python3 create_gif.py --image_folder 'results/' --output_gif 'upscaled_frames.gif' --_format 'png'

echo "CONTROL: starting to create the small photo gif"
#python3 create_gif.py --image_folder 'LR/' --output_gif 'small_frames.gif' --_format 'jpg'