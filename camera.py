import numpy as numpy
from cv2 import CascadeClassifier
import cv2  
import sys
import pickle

labels={}
with open("labels.pickle",'rb') as f :
    org_labels = pickle.load(f)
    labels = {v:k for k,v in org_labels.items()}


def find_faces():
        face_cascade = CascadeClassifier('haarcascade_frontalface_default.xml')
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read("trainer.yml")

        lefteye_cascade = CascadeClassifier('haarcascade_lefteye.xml')
        video_capture = cv2.VideoCapture(0)

        while True:
            #Capture Frame by Frame 
            ret, frame = video_capture.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)

            #Draws a rectagle around the face
            for(x, y, w, h) in faces:
                frame = cv2.rectangle(frame, (x, y,), (x+w, y+h), (0, 255, 0), 3)
                roi_gray= gray[y:y+h, x:x+w]
                roi_color= frame[y:y+h, x:x+w]
                eyes= lefteye_cascade.detectMultiScale(roi_gray)
                # id_,conf = recognizer.predict(eyes)
                # if conf>=85:
                #     print(id_)
                #     name = labels[id_]
                #     font = cv2. FONT_HERSHEY_SIMPLEX
                #     color = (255,255,255)
                #     stroke = 2
                #     cv2.putText(frame, name, (x,y), font, 1, color, stroke, cv2.LINE_AA)

                #     for (ex,ey,ew,eh) in eyes:
                #         cv2.rectangle(roi_color,(ex,ey),(ex+ew, ey+eh), (255,0,0),3)
                # else:
                    # for (ex,ey,ew,eh) in eyes:
                    #     cv2.rectangle(roi_color,(ex,ey),(ex+ew, ey+eh), (255,0,255),3)
                for (ex,ey,ew,eh) in eyes:
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew, ey+eh), (255,0,255),3)
                    

            #Dipsplay the resulting frame
            cv2.imshow('Video',frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        video_capture.release()
        cv2.destroyAllWindows()

find_faces()