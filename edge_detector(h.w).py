import cv2
import numpy as np

cap = cv2.VideoCapture(0)
current_mode = "Original"
gaussian_kernel = 5
median_kernel = 5
canny_kernel = 100

while True:
    ret,frame = cap.read()
    if not ret:
        break
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    output =  frame.copy()
    
    if current_mode == "laplacian":
        lap = cv2.Laplacian(gray, cv2.CV_64F)
        output = cv2.cvtColor(np.uint8(np.absolute(lap)), cv2.COLOR_GRAY2BGR)
        
    elif current_mode == "gaussian":
        if gaussian_kernel % 2 == 0:
            gaussian_kernel += 1
        output = cv2.GaussianBlur(frame, (gaussian_kernel,gaussian_kernel),0)
        
    elif current_mode == "median":
        if median_kernel % 2 == 0:
            median_kernel += 1
        output = cv2.medianBlur(frame,median_kernel)
    
    elif current_mode == "canny":
        if canny_kernel % 2 == 0:
            canny_kernel += 1
        blur = cv2.GaussianBlur(frame, (5, 5), 1.4)
        output = cv2.Canny(blur,threshold1=100, threshold2=200)

    cv2.putText(output, f'mode = {current_mode}',(10,30),
                cv2.FONT_HERSHEY_SIMPLEX, 1,(0,255,255),2)
    
    cv2.imshow("Live Filter Detection",output)
    
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('q'):
        break
    elif key == ord('l'):
        current_mode = "laplacian"
    elif key == ord('g'):
        current_mode = "gaussian"
    elif key == ord('m'):
        current_mode = "median"
    elif key == ord('o'):
        current_mode = "original"
    elif key == ord('c'):
        current_mode = "canny"

        
    elif key == ord('+') and current_mode == "gaussian":
        gaussian_kernel +=2
    elif key == ord('-') and current_mode == "gaussian":
        gaussian_kernel = max(1, gaussian_kernel -2)
    elif key == ord("]") and current_mode == "median":
        median_kernel += 2
    elif key == ord('[') and current_mode == "median":
        median_kernel = max(1,median_kernel-2)
        
cap.release()
cv2.destroyAllWindows()