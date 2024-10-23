#Make sure to adjust the frame extraction rate if needed (e.g., extract every nth frame).
#This script saves frames sequentially in extracted_frames/ as frame_0000.jpg, frame_0001.jpg, etc.
import cv2
import os

# Set the range of frames to extract
start_frame = 1  # Starting frame (inclusive)
end_frame = 145    # Ending frame (inclusive)

# Load the video file
video_path = 'flowers.mp4'
video = cv2.VideoCapture(video_path)

# Check if the video file was opened successfully
if not video.isOpened():
    print("Error opening video file")

# Create a directory to store the extracted frames
output_dir = 'extracted_frames'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Initialize variables
frame_count = 0
success = True

# Loop through the video
while success:
    success, frame = video.read()
    
    if success and frame_count >= start_frame:
        # Save the frame only if it is within the specified range
        if start_frame <= frame_count <= end_frame:
            frame_path = os.path.join(output_dir, f'frame_{frame_count:04d}.jpg')
            cv2.imwrite(frame_path, frame)
            #print(f"Extracted frame {frame_count}")
        elif frame_count > end_frame:
            break  # Stop once the end_frame is reached
    
    frame_count += 1

# Release the video capture object
video.release()
print(f"Frames {start_frame} to {end_frame} extracted and saved to {output_dir}")
