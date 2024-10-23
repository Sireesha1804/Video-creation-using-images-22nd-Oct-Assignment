import cv2
import os

# Directory containing images
image_folder = 'C:/Users/shire/Downloads/pizzas'
# Video output
video_name = 'pizzaas_video.mp4'

# desired frame rate (FPS)
fps = 30

# duration for each image 
image_duration = 2  

# Get a list of image file names
images = [img for img in os.listdir(image_folder) if img.endswith(".jpg") or img.endswith(".png")]
# Sort the images by name or some other logic
images.sort()

# Read the first image to determine the video frame size
first_image_path = os.path.join(image_folder, images[0])
frame = cv2.imread(first_image_path)
height, width, layers = frame.shape

# Create a VideoWriter object
video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

# Loop through all images, resize them if necessary, and write them to the video
for image in images:
    img_path = os.path.join(image_folder, image)
    frame = cv2.imread(img_path)
    
    # Resize frame to match the first image's resolution
    resized_frame = cv2.resize(frame, (width, height))
    
    # Write the same frame multiple times to achieve the desired duration
    for _ in range(int(fps * image_duration)): 
        video.write(resized_frame)

# Release the video writer object
video.release()

print("Video saved as {video_name}")


