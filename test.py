import os.path as osp
import glob
import cv2
import numpy as np
import torch
import RRDBNet_arch as arch
import os
import argparse
import os

# Argument parsing
parser = argparse.ArgumentParser()
parser.add_argument("--video_name",    default = 'video',                            type = str, help = "video name")
parser.add_argument("--model_path",    default = 'models/RRDB_ESRGAN_x4.pth',        type = str, help = "resize percentage (e.g., 50 for 50%)")
parser.add_argument("--input_dir",     default = None,      type = str, help = "input directory for images")
parser.add_argument("--output_dir",    default = None,      type = str, help = "output directory for resized images")

args = parser.parse_args()

# Set input and output directories
video_name  = args.video_name
input_dir   = args.input_dir  if args.input_dir  else f'extracted_frames_{video_name}_LR'
output_dir  = args.output_dir if args.output_dir else f'extracted_frames_{video_name}_HD'
# Create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

model_path =  args.model_path # models/RRDB_ESRGAN_x4.pth OR models/RRDB_PSNR_x4.pth
#device = torch.device('cuda')  # if you want to run on CPU, change 'cuda' -> cpu
device = torch.device('cpu')

test_img_folder = f'{input_dir}/*'

model = arch.RRDBNet(3, 3, 64, 23, gc=32)
model.load_state_dict(torch.load(model_path, weights_only=True), strict=True)
model.eval()
model = model.to(device)

print('Model path {:s}. \nTesting...'.format(model_path))

idx = 0
for path in glob.glob(test_img_folder):
    idx += 1
    base = osp.splitext(osp.basename(path))[0]
    print(idx, base)
    # read images
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    img = img * 1.0 / 255
    img = torch.from_numpy(np.transpose(img[:, :, [2, 1, 0]], (2, 0, 1))).float()
    img_LR = img.unsqueeze(0)
    img_LR = img_LR.to(device)

    with torch.no_grad():
        output = model(img_LR).data.squeeze().float().cpu().clamp_(0, 1).numpy()
    output = np.transpose(output[[2, 1, 0], :, :], (1, 2, 0))
    output = (output * 255.0).round()
    cv2.imwrite(''+str(output_dir)+'/{:s}_HD.png'.format(base), output)
