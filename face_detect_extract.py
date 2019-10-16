import cv2
import sys
import os
dirname = "C:\\xampp\\htdocs\\prakalpa\\temp\\"
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
    i=0
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        sub_face = image[y:y+h, x:x+w]
        face_file_name = dirname+"extracted_" + str(i) + ".png"
        cv2.imwrite(face_file_name, sub_face)
        i+=1

    #cv2.waitKey(0)
