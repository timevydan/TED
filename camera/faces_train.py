import os
import numpy as np
from PIL import Image
import pickle
import cv2
from skimage.io import imread


def train_faces():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    image_dir = os.path.join(BASE_DIR, "images")

    face_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
    lefteye_cascade = cv2.CascadeClassifier('haarcascade/haarcascade_lefteye.xml')
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
                pil_image = imread(path)
                pil_image = cv2.cvtColor(pil_image, cv2.COLOR_BGR2GRAY)
                pil_image2 = cv2.resize(pil_image, None, fx=1, fy=1,interpolation=cv2.INTER_CUBIC)
                image_array = np.array(pil_image2, "uint8")
                pil_image3 = cv2.resize(pil_image, None, fx=1.5, fy=1.5,interpolation=cv2.INTER_CUBIC)
                image_array = np.array(pil_image3, "uint8")
                # print(image_array)
                faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.25, minNeighbors=1)
                for(x, y, w, h) in faces: 
                    roi = image_array[y:y+h, x:x+w]
                    print(roi)
≈                    x_train.append(roi)
                    y_labels.append(id_)

    with open("labels.pickle",'wb') as f :
        pickle.dump(label_ids,f)

    recognizer.train(x_train, np.array(y_labels))
    recognizer.save("trainer.yml")

if __name__ == "__main__":
    train_faces()
