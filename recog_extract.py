import cv2,os,sys,pickle
from face_recognition import load_image_file, face_locations, face_encodings, compare_faces
import numpy as np

def encoding(x):
    temp = face_encodings(load_image_file(x))
    if temp:
        return (temp[0],1)
    else:
        return (temp,0)

dirname = "C:\\xampp\\htdocs\\prakalpa\\temp\\"

with open("imgdb.pkl", 'rb') as f:
    imgdb = pickle.load(f)
known_face_encodings = imgdb[0]
known_face_names = imgdb[1]
face_names = []
# Get user supplied values
try:
    imagePath = sys.argv[1]
    cascPath = "haarcascade_frontalface_default.xml"
except:
    exit()
else:
    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)

    # Read the image
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
        #flags = cv2.CV_HAAR_SCALE_IMAGE
    )

    #print("Found {0} faces!".format(len(faces)))
    i = 0
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        sub_face = image[y:y+h, x:x+w]
        face_file_name = dirname+"extracted_" + str(i) + ".png"
        cv2.imwrite(face_file_name, sub_face)
        temp,t = encoding(face_file_name)
        if t:
            matches = compare_faces(known_face_encodings,temp )
            name = "Unknown"

    # If a match was found in known_face_encodings, just use the first one.
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
                face_names.append(name)
        i += 1
    with open("C:\\xampp\\htdocs\\prakalpa\\temp\\list.txt", 'w') as f:
       f.writelines("%s\n" % i for i in face_names)
if len(face_names)<i:
    print(1)
else:
    print(0)
    
