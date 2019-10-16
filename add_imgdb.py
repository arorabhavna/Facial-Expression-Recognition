import cv2
import os
import sys
import pickle
from face_recognition import load_image_file, face_locations, face_encodings, compare_faces
import numpy as np
import csv

def encoding(x):
    temp = face_encodings(load_image_file(x))
    if temp:
        return (temp[0], 1)
    else:
        return (temp, 0)


dirname = "C:\\xampp\\htdocs\\prakalpa\\temp\\"

with open("imgdb.pkl", 'rb') as f:
    imgdb = pickle.load(f)
print(imgdb)
name=sys.argv[1]
file = sys.argv[2]
age = sys.argv[3]
gender = sys.argv[4]
education = sys.argv[5]
profession = sys.argv[6]
if name=="" or file=="" or age=="" or gender=="" or education=="" or profession=="":
    print("No Null Values allowed !")

elif name in imgdb[1]:
    print("Name Already in Database")
else:
    imgdb[1].append(name)
    imgdb[0].append(encoding(file)[0])
    with open("imgdb.pkl", 'wb') as f:
        imgdb = pickle.dump(imgdb,f)
    fields = [name,age,gender,education,profession]
    with open('database.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
    print("Successfully Added !")
