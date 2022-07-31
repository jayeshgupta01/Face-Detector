# -*- coding: utf-8 -*-
"""
Created on Thu May 14 14:13:02 2020

@author: HP
"""

import cv2
faceCascade = cv2.CascadeClassifier('F:\py\haarcascade_frontalface_default.xml')
print("Press q to quit")
video_capture = cv2.VideoCapture(0)
while True:
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,1.3,4)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, "Number of faces detected: " + str(faces.shape[0]), (0,frame.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (255,0,0), 1)
        #total=math.count(cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2))
        cv2.imshow('FaceDetection', frame)
        
    k=cv2.waitKey(1) 
    if k==ord('q'): 
        break

video_capture.release()
cv2.destroyAllWindows()