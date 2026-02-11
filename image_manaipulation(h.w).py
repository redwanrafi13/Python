import cv2
import numpy as np
from datetime import datetime

y_start, y_end = 0, 240
x_start, x_end = 0, 320

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

brightness = 0
is_gray = False
rotation_angle = 0
flip_mode = None

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    img = frame.copy()
    
    cropped_frame = frame[y_start:y_end, x_start:x_end]
    
    if is_gray:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        
    img =cv2.convertScaleAbs(img, alpha= 1 , beta= brightness )
    
    if rotation_angle != 0:
        h, w = img.shape[:2]
        matrix = cv2.getRotationMatrix2D((w // 2, h // 2), rotation_angle, 1)
        img = cv2.warpAffine(img,matrix, (w,h))
        
    if flip_mode is not None:
        img = cv2.flip(img, flip_mode)
        

    cv2.imshow('Original Live Feed', frame)
    
    key= cv2.waitKey(1) & 0xFF
    
    if key == ord('q'):
        break
    if key == ord('g'):
        is_gray = not is_gray
    if key == ord('b'):
        brightness += 10
    if key == ord('n'):
        brightness -= 10
    if key == ord('l'):
        rotation_angle -= 90
    if key == ord('r'):
        rotation_angle += 90
    if key == ord('h'):
        flip_mode = None if flip_mode == 1 else 1
    if key == ord('s'):
        filename = f"photo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
        cv2.imwrite(filename,frame)
        print(f"Saved: {filename}")
    if key == ord('c'):
        cv2.imshow('Cropped Feed (ROI)', cropped_frame)
    
cap.release()
cv2.destroyAllWindows()