import cv2
import glob

# Resize frames to 50% of their original size
for img_path in glob.glob('LR/*.jpg'):
    img = cv2.imread(img_path)
    small_img = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2))
    cv2.imwrite(img_path, small_img)