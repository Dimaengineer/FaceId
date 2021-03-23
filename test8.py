import numpy as np
import face_recognition
import cv2
import os
from datetime import datetime
from tkinter import *
import time
from VideoCapture import Device
from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication, QWidget
import sys
path = 'dataset'
images = []
classNames = []
classWho = []
myList = os.listdir(path)

for mylist in myList:
    curImg = cv2.imread(f'{path}/{mylist}')
    images.append(curImg)
    classNames.append(os.path.splitext(mylist)[0].replace("buyer", "").replace("seller", ""))
    classWho.append(os.path.splitext(mylist)[0].replace(os.path.splitext(mylist)[0].replace("buyer", "").replace("seller", ""), ""))


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def markAttendance(name):
    with open("Attendance.csv", "r+") as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime("%H:%M:%S")
            f.writelines(f'\n{name}, {dtString}')

encodeListKnown = findEncodings(images)

cap = cv2.VideoCapture(0)
s = []
w = []
while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)
    
    for encodeFace, faceLoc in zip(encodeCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        #print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            global name
            name = classNames[matchIndex]
            who = classWho[matchIndex]
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            markAttendance(name)
            if who == "seller":
                if not name in s:
                    print(f"Привет {name} за работу")
                    s.append(name)
            if who == "buyer":
                if not name in s:
                    print(f"Привет {name} хороших покупок")
                    s.append(name)
        elif matchIndex != matches[matchIndex]:
            time.sleep(2)
            if not "Регистрацыя"  in s:
                print(f"Регистрацыя")
                s.append("Регистрацыя")
            Name = input("name ")
            Who = input("who you(buyer, seller)")
            if Who == "seller" or "buyer":
                path = "C:\python388\prog\dataset"
                cv2.imwrite(os.path.join(path ,Name + Who + '.jpg'), img)
                myList = os.listdir(path)

                for cls in myList:
                    curImg = cv2.imread(f'{path}/{cls}')
                    images.append(curImg)
                    classNames.append(os.path.splitext(cls)[0].replace("buyer", "").replace("seller", ""))
                    classWho.append(os.path.splitext(cls)[0].replace(os.path.splitext(cls)[0].replace("buyer", "").replace("seller", ""), ""))


                def findEncodings(images):
                    encodeList = []
                    for img in images:
                        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                        encode = face_recognition.face_encodings(img)[0]
                        encodeList.append(encode)
                    return encodeList
                encodeListKnown = findEncodings(images)

