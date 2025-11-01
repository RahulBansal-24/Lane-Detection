# importing required libraries

import cv2, numpy as np, tkinter as tk

from tkinter import filedialog

#taking video file input from user
root = tk.Tk()
root.withdraw()  # hiding the main tkinter window
video_path = filedialog.askopenfilename(
    title="Select a video file",
    filetypes=[("Video files", "*.mp4 *.avi *.mov *.mkv")]
)

if not video_path:
    print("No file selected. Exiting.")
    exit()

#defining process_frame function
def process_frame(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    kernel_size = 3
    blur_gray = cv2.GaussianBlur(gray,(kernel_size,kernel_size),0)
    low_threshold = 100
    high_threshold = 150
    edges = cv2.Canny(blur_gray,low_threshold,high_threshold)
    
    mask = np.zeros_like(edges)
    mask_color = 255
    
    imshape = image.shape
    vertices = np.array([[(0,imshape[0]), (200,int(imshape[0]/1.7)), (int(imshape[1]-200), int(imshape[0]/1.7)), (imshape[1], imshape[0])]], dtype=np.int32)
    
    mask = cv2.fillPoly(mask,vertices,mask_color)
    masked_edges = cv2.bitwise_and(edges,mask)
    
    #find all straight lines in image return their (x1,y1),(x2,y2) coordinates
    rho = 5
    theta = np.pi/180
    threshold = 100
    min_line_length = 80
    max_line_gap = 200
    line_image = np.zeros_like(image)
    
    lines = cv2.HoughLinesP(masked_edges, rho, theta, threshold, np.array([]), min_line_length, max_line_gap)
    
    if lines is not None:
        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 5)
    
    # overlay lines on the original image
    combo = cv2.addWeighted(image, 0.8, line_image, 1, 0)
    
    return combo
    
    
    

# Loading the video using openCV and this function sets isOpened function to True
vid = cv2.VideoCapture(video_path)

while vid.isOpened():
    flag, frame = vid.read() #this function reads first frame and keeps incrementing
    if not flag:
        print("video ended or video broke")
        break
    
    #frames are received in BGR format converting them to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #processing the frame
    processed_frame = process_frame(frame_rgb)
    
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    processed_frame = process_frame(frame_rgb)
    
    # Convert back to BGR for display in OpenCV window
    processed_bgr = cv2.cvtColor(processed_frame, cv2.COLOR_RGB2BGR)
    cv2.imshow("Lane Detection", processed_bgr)
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

#closing video file
vid.release()
cv2.destroyAllWindows()