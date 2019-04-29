import numpy as numpy
from cv2 import CascadeClassifier
import cv2
import sys
import pickle


def find_faces():
    labels = {}
    with open("./labels.pickle", 'rb') as f:
        org_labels = pickle.load(f)
        labels = {v: k for k, v in org_labels.items()}

    face_cascade = CascadeClassifier(
        './haarcascade/haarcascade_frontalface_default.xml')
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("./trainer.yml")

    lefteye_cascade = CascadeClassifier('./haarcascade/haarcascade_lefteye.xml')
    video_capture = cv2.VideoCapture(0)
    picture_counter = 0

    picture_flag = False
    while True:
        # Capture Frame by Frame
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(
            gray, scaleFactor=1.05, minNeighbors=8)
        face_dic = {
            "known": 0,
            "total": 0}
        # Draws a rectagle around the face
        for(x, y, w, h) in faces:
            face_dic["total"] += 1
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            id_, conf = recognizer.predict(roi_gray)
            eyes = lefteye_cascade.detectMultiScale(roi_gray)
            test = [i for i in eyes]
            if test:
                frame = cv2.rectangle(
                    frame, (x, y,), (x+w, y+h), (0, 255, 0), 3)

            # conf  is the confidence level that detected face has been trained
            if conf >= 85:
                print(id_)
                face_dic["known"] += 1
                name = labels[id_]
                font = cv2. FONT_HERSHEY_SIMPLEX
                color = (255, 255, 255)
                stroke = 2
                cv2.putText(frame, name, (x, y), font, 1,
                            color, stroke, cv2.LINE_AA)

                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey),
                                  (ex+ew, ey+eh), (255, 0, 0), 3)
            else:
                for (ex, ey, ew, eh) in eyes:
                    cv2.rectangle(roi_color, (ex, ey),
                                  (ex+ew, ey+eh), (255, 0, 255), 3)
        
        
        # Shows Number faces dectected/known in frame
        cv2.putText(frame, "Number of faces detected: " + str(
            face_dic["total"]),  (0, 100), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (255, 0, 0), 1)
        cv2.putText(frame, "Number of faces known: " + str(
            face_dic["known"]),  (0, 120), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (255, 0, 0), 1)

        # Dipsplay the resulting frame
        cv2.imshow('Video', frame)
        
        
        #Saves Picture 
        if face_dic["known"] == 0 and face_dic["total"] >= 1:
            if picture_flag == False:
                picture_counter += 1
                cv2.imwrite("./test_subjects/" +
                            str(picture_counter)+".png", frame)
                picture_flag = True
            picture_counter += 1
            if picture_counter == 120:
                picture_flag = False
                picture_counter = 0

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()
if __name__ == "__main__":
    find_faces()