import numpy as np
import face_recognition
import cv2
import os
from datetime import datetime
import time

# Define the dataset path
path = 'dataset'
os.makedirs(path, exist_ok=True)
images = []
classNames = []
classWho = []
myList = os.listdir(path)

# Load images and extract class names and roles (buyer/seller)
for mylist in myList:
    curImg = cv2.imread(f'{path}/{mylist}')
    images.append(curImg)
    classNames.append(os.path.splitext(mylist)[0].replace("buyer", "").replace("seller", ""))
    classWho.append(os.path.splitext(mylist)[0].replace(os.path.splitext(mylist)[0].replace("buyer", "").replace("seller", ""), ""))

# Function to find encodings for the images
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)
        if encode:
            encodeList.append(encode[0])
    return encodeList

# Function to mark attendance in a CSV file
def markAttendance(name):
    with open("Attendance.csv", "a") as f:
        dtString = datetime.now().strftime("%H:%M:%S")
        f.write(f'{name}, {dtString}\n')

# Encode known images
encodeListKnown = findEncodings(images)

# Initialize webcam
cap = cv2.VideoCapture(0)
s = []

# Process each frame from the webcam
while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture image")
        continue

    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodeCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

        if faceDis.size > 0:
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex]
                who = classWho[matchIndex]
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                markAttendance(name)
                if who == "seller":
                    if name not in s:
                        print(f"Привет {name}, за работу!")
                        s.append(name)
                elif who == "buyer":
                    if name not in s:
                        print(f"Привет {name}, хороших покупок!")
                        s.append(name)
        else:
            time.sleep(2)
            if "Регистрацыя" not in s:
                print("Регистрацыя")
                s.append("Регистрацыя")
            Name = input("Name: ")
            Who = input("Who are you (buyer/seller): ").strip().lower()
            if Who in ["seller", "buyer"]:
                cv2.imwrite(os.path.join(path, f"{Name}{Who}.jpg"), img)
                images.append(cv2.imread(f'{path}/{Name}{Who}.jpg'))
                classNames.append(Name)
                classWho.append(Who)
                encodeListKnown = findEncodings(images)

    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
