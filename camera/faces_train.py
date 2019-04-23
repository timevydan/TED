import os
import numpy as np
from PIL import Image
import pickle
import cv2


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "images")

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
lefteye_cascade = cv2.CascadeClassifier('haarcascade_lefteye.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

current_id = 0
label_ids = {}
y_labels = []
x_train = []

for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg"):
            path = os.path.join(root, file)
            label = os.path.basename(root).replace(" ", "-").lower()

            print(label, path)
            if  not label in label_ids:
                label_ids[label] = current_id
                current_id +=1
            id_ = label_ids[label]
            
            pil_image = Image.open(path).convert("L")  # converst to grayscale
            image_array = np.array(pil_image, "uint8")
            # print(image_array)
            faces = face_cascade.detectMultiScale(image_array,scaleFactor=1.05, minNeighbors=5)
            for(x, y, w, h) in faces: 
                roi = image_array[y:y+h, x:x+w]
                eye= lefteye_cascade.detectMultiScale(roi)
                for (ex,ey,ew,eh) in eye:
                    roi_eye = lefteye_cascade.detectMultiScale(roi, scaleFactor=1.05, minNeighbors=3)
                    print(roi_eye)

                    x_train.append(roi_eye)
                    y_labels.append(id_)

with open("labels.pickle",'wb') as f :
    pickle.dump(label_ids,f)

recognizer.train(x_train, np.array(y_labels))
recognizer.save("trainer.yml")
