import numpy as numpy
from cv2 import CascadeClassifier
import cv2  
import sys


face_cascade = CascadeClassifier('haarcascade_frontalface_default.xml')
video_capture = cv2.VideoCapture(0)

while True:
    #Capture Frame by Frame 
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.25, minNeighbors=5)

    #Draws a rectagle around the face
    for(x, y, w, h) in faces:
        frame = cv2.rectangle(frame, (x, y,), (x+w, y+h), (0, 255, 0), 3)

    #Dipsplay the resulting frame
    cv2.imshow('Video',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()