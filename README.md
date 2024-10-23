Made in Vancouver, Canada by  [Sebanthalas](https://sites.google.com/view/sebanthalas), October 2024
 


This folder contains the solution to an enquiry from [private company] for a job application  to Senior Photo Effect Improvements and Good Photos Auto Filtering Developer.


* Made on Linux (x86_64)
 
# Image_Enhancement
This project demonstrates a full pipeline from extracting video frames from [HD flower video](https://youtu.be/4N8oOj_aue8?si=Xpd3pacA9njWu6sC) to applying super-resolution techniques using [ESRGAN](https://arxiv.org/pdf/1809.00219), finishing with a visual representation in the form of a GIF. It is designed to highlight my ability to work with video processing, machine learning pre-trained models, and data visualization.

Requirements

* Python 3.x
* Pillow library: pip3 install pillow
* OpenCV for Python (for frame extraction)
* PyTorch (for running ESRGAN)
* ESRGAN model files
  
Files:
The source video in .mp4 can be obtained from [here](https://drive.google.com/drive/folders/1X444iFtM6SDBYem50u-ZzUZTGaf84MdR?usp=drive_link).
The scripts can be downloaded from the github repository.

## Project Overview

This project demonstrates how to upscale low-resolution video frames using [ESRGAN](https://arxiv.org/pdf/1809.00219) (Enhanced Super-Resolution Generative Adversarial Networks). The goal is to extract specific frames from a video, apply super-resolution techniques to enhance their quality, and create a GIF to visualize the improvement.

![frame_0001](https://github.com/user-attachments/assets/253ceaaf-c232-434d-a615-1600fc7d46bf)![frame_0001_rlt](https://github.com/user-attachments/assets/75db13e4-1bd7-4b75-af8f-d552e10a6ea9) 

Link to the comparison gif (low and high quality): [GIF](https://drive.google.com/drive/folders/1X444iFtM6SDBYem50u-ZzUZTGaf84MdR?usp=drive_link)

## Step by Step
 I can provide a step-by-step guide on how to run the code and test it upon the company's request.
 
## Possible improvements to deal with blur cause by movement

Using ESRGAN (or similar super-resolution models) alone is not specifically designed to address motion blur in videos, although it can improve the overall sharpness and resolution. Super-resolution models like ESRGAN focus on upscaling images and adding fine detail to low-resolution images, but they don't inherently fix issues like motion blur caused by movement or camera shake in the source frames.

However, there are other techniques and tools that we can combine with ESRGAN to handle motion blur more effectively:
 * Use the pre-trained models to apply deblurring to our extracted frames before using ESRGAN for upscaling.  DeblurGAN also uses PyTorch and it is a GAN-based model designed specifically for image deblurring.
 * If we are still seeing some blur after running DeblurGAN, we might need to fine-tune the deblurring process by trying different pre-trained models or adjusting hyperparameters, such as kernel size, when using traditional deblurring algorithms.

There are some interesting works in this topic. After a quick search I found some interesting starting points that may be useful:
* [Learning to See in the Dark](https://arxiv.org/abs/1805.01934) (paper with code, cited 1405 times )
* [Stereoscopic video deblurring transformer ](https://www.nature.com/articles/s41598-024-63860-9) (recent article)
* [Fast Ultra High-Definition Video Deblurring via Multi-scale Separable Network](https://link.springer.com/article/10.1007/s11263-023-01958-9)

## Final comment

I am confident that my coding skills are well-suited to meet this challenge. I recognize that thorough research is essential in order to propose an action plan. My strong mathematical background allows me to efficiently navigate the latest developments in deblurring techniques and offer well-founded recommendations for the next steps, including implementation suggestions. After conducting this research, I am convinced that the necessary techniques are within reach, and successful implementation will require a robust mathematical foundation to ensure precision and effectiveness. I look forward to the opportunity to further discuss how my skills and experiences can contribute to your team's success.







 
