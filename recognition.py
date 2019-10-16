from face_recognition import load_image_file, face_locations, face_encodings, compare_faces
import pickle
import sys

with open("imgdb.pkl", 'rb') as f:
    imgdb = pickle.load(f)


def encoding(x): return face_encodings(load_image_file(x))[0]


known_face_encodings = imgdb[0]
known_face_names = imgdb[1]

image = load_image_file(sys.argv[1])
face_locations = face_locations(image)
face_encodings = face_encodings(image, face_locations)

face_names = []
for face_encoding in face_encodings:
    # See if the face is a match for the known face(s)
    matches = compare_faces(
        known_face_encodings, face_encoding)
    name = "Unknown"

    # If a match was found in known_face_encodings, just use the first one.
    if True in matches:
       first_match_index = matches.index(True)
       name = known_face_names[first_match_index]
       face_names.append(name)


with open("list.txt", 'w') as f:
    f.writelines("%s\n" % i for i in face_names)
