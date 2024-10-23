#!/bin/bash -vv

python --version

echo "CONTROL: starting extract the frames from the video"
python3 extract.py

echo "CONTROL: starting making the image even smaller"
python3 smaller_image.py

echo "CONTROL: starting to run ESRGAN model"
#python3 ESRGAN/test.py --model_path models/RRDB_ESRGAN_x4.pth --input_folder LR --output_folder results

echo "CONTROL: starting to create the upscaled gif"
python3 create_gif.py --image_folder 'results/' --output_gif 'upscaled_frames.gif' --_format 'png'

echo "CONTROL: starting to create the small photo gif"
python3 create_gif.py --image_folder 'LR/' --output_gif 'small_frames.gif' --_format 'jpg'