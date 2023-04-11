import cv2
import face_recognition
import csv
import numpy as np
from datetime import datetime

video_capture = cv2.VideoCapture(0)

# load known faces
sobia_image=face_recognition.load_image_file("faces/sobia.jpg")
sobia_encoding=face_recognition.face_encodings(sobia.jpg)[0]

known_face_encodings=[sobia_encoding]
known_face_names=["sobia"]

#list of expected students
students=known_face_names.copy()

face_locations=[]
face_encodings=[]

#Get time and date
now= datetime.now()
current_date=now.strftime("%Y-%m-%d")

# create file to store data
f = open(f"{current_date}.csv","w+",newline="")
lnwriter=csv.writer(f)

while True:
    _, frame=video_capture.read()
    small_frame=cv2.resize(frame,(0,0),fx=0.25, fy=0.25)
    rgb_small_frame= cv2.cvtColor(small_frame, cv2.COLOR_BG2BGR)

 #Recognizing faces
    face_locations=face_recognition.face_locations(rgb_small_frame)
    face_locations=face_recognition.face_locations(rgb_small_frame,face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings,face_encoding)
        face_distance=face_recognition.face_distance(known_face_encodings,face_encoding)
        best_match_index = np.argmin(face_distance)

        if(matches[best_match_index]):
            nama=known_face_names[best_match_index]

        cv2.imshow("Attendance",frame)
        if cv2.waitKey(1) & 0xFF==ord("q"):
            break

