import cv2
from keras.models import model_from_json
import numpy as np
from datetime import datetime

# from keras_preprocessing.image import load_img
json_file = open("emotiondetector.json", "r")
model_json = json_file.read()
json_file.close()
model = model_from_json(model_json)

model.load_weights("emotiondetector.h5")
haar_file=cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade=cv2.CascadeClassifier(haar_file)


labels = {0 : 'angry', 1 : 'happy', 2 : 'neutral', 3 : 'sad', 4 : 'tired'}
count_emotions = {'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'happy': 0, 'angry': 0, 'neutral': 0, 'sad': 0, 'tired': 0, 
                  'r': 0, 'g': 0, 'b': 0}
MAX_PEOPLE = 1


webcam=cv2.VideoCapture(0)

def extract_features(image):
    feature = np.array(image)
    feature = feature.reshape(1,48,48,1)
    return feature/255.0

def getRecog():
    while True:
        i,im=webcam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(im,1.3,5)
        try: 
            for (p,q,r,s) in faces:
                image = gray[q:q+s,p:p+r]
                cv2.rectangle(im,(p,q),(p+r,q+s),(255,0,0),2)
                image = cv2.resize(image,(48,48))
                img = extract_features(image)
                pred = model.predict(img)
                prediction_label = labels[pred.argmax()]
                c = 0
                for i in labels:
                    if prediction_label.__eq__(labels[i]):
                        c += 1
                        count_emotions[prediction_label] = c
                    else:
                        count_emotions[labels[i]] = 0
                # print(count_emotions)
                # print("Predicted Output:", prediction_label)
                cv2.putText(im, '% s' %(prediction_label), (p-10, q-10),cv2.FONT_HERSHEY_COMPLEX_SMALL,2, (0,0,255))
            cv2.imshow("Output",im)
            cv2.waitKey(27)
        except cv2.error:
            pass


def getcount_emotions():
    return count_emotions


def getcount_emotionsarray():
    return [count_emotions['angry'], count_emotions['disgust'], count_emotions['fear'],
            count_emotions['happy'], count_emotions['neutral'], count_emotions['sad'], 
            count_emotions['surprise']]


def test():
    getRecog()