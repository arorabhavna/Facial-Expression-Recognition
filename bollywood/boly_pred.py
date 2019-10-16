import face_recognition,pickle
import csv
"""alia_image = face_recognition.load_image_file("alia.jpg")
alia_face_encoding = face_recognition.face_encodings(alia_image)[0]

varun_image = face_recognition.load_image_file("varun.jpg")
varun_face_encoding = face_recognition.face_encodings(varun_image)[0]

bhumi_image = face_recognition.load_image_file("bhumi.jpg")
bhumi_face_encoding = face_recognition.face_encodings(bhumi_image)[0]

ranbir_image = face_recognition.load_image_file("ranbir.jpeg")
ranbir_face_encoding = face_recognition.face_encodings(ranbir_image)[0]

ayush_image = face_recognition.load_image_file("ayushman.jpg")
ayush_face_encoding = face_recognition.face_encodings(ayush_image)[0]

karan_image = face_recognition.load_image_file("karan.jpg")
karan_face_encoding = face_recognition.face_encodings(karan_image)[0]

vicky_image = face_recognition.load_image_file("vicky.jpg")
vicky_face_encoding = face_recognition.face_encodings(vicky_image)[0]

rohit_image = face_recognition.load_image_file("rohit.jpg")
rohit_face_encoding = face_recognition.face_encodings(rohit_image)[0]

modi_image = face_recognition.load_image_file("modi.jpg")
modi_face_encoding = face_recognition.face_encodings(modi_image)[0]

ranveer_image = face_recognition.load_image_file("ranveer.jpg")
ranveer_face_encoding = face_recognition.face_encodings(ranveer_image)[0]

raj_image = face_recognition.load_image_file("rajkumar.jpg")
raj_face_encoding = face_recognition.face_encodings(raj_image)[0]


known_face_encodings = [alia_face_encoding,varun_face_encoding,bhumi_face_encoding,ranbir_face_encoding,ayush_face_encoding,karan_face_encoding,vicky_face_encoding,rohit_face_encoding,modi_face_encoding,ranveer_face_encoding,raj_face_encoding]
known_face_names = ["alia","varun","bhumi","ranbir","ayush","karan","vicky","rohit","modi","ranveer","rajkumar"]

image = face_recognition.load_image_file("boly.jpg")
face_locations = face_recognition.face_locations(image)
face_encodings = face_recognition.face_encodings(image, face_locations)

face_names = []
for face_encoding in face_encodings:
    # See if the face is a match for the known face(s)
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    name = "Unknown"

    # If a match was found in known_face_encodings, just use the first one.
    if True in matches:
       first_match_index = matches.index(True)
       name = known_face_names[first_match_index]

    face_names.append(name)

print(face_names)
imgdb = [[alia_face_encoding, varun_face_encoding, bhumi_face_encoding, ranbir_face_encoding, ayush_face_encoding,
          karan_face_encoding, vicky_face_encoding, rohit_face_encoding, modi_face_encoding, ranveer_face_encoding, raj_face_encoding], ["alia", "varun", "bhumi", "ranbir", "ayush", "karan", "vicky", "rohit", "modi", "ranveer", "rajkumar"]]
with open("imgdb.pkl", 'wb') as f:
        imgdb = pickle.dump(imgdb, f)"""
fields = ["skanda","18","male","BE","student"]
with open('database.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
