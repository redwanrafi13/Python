import cv2
import numpy as np
import os

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


cap = cv2.VideoCapture(0)

face_id = 0


if not os.path.exists("detected_faces"):
    os.makedirs("detected_faces")

while True:

    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(30,30)
    )

    
    face_count = len(faces)

    for (x, y, w, h) in faces:

        
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

        
        cv2.putText(frame, "Face Detected", (x,y-10),
        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0),2)

        
        face_img = frame[y:y+h, x:x+w]
        cv2.imwrite(f"detected_faces/face_{face_id}.jpg", face_img)

        face_id += 1

    
    cv2.putText(frame, f"Faces: {face_count}", (10,30),
    cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0),2)

    cv2.imshow("Advanced Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()