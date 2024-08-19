import face_recognition
import cv2
import os
import shutil

# Getting reference encodings
reference_image = cv2.imread("./reference_image/DSC_2180.JPG")
ref_rgb_image = cv2.cvtColor(reference_image, cv2.COLOR_BGR2RGB)
ref_face_locations = face_recognition.face_locations(ref_rgb_image)
ref_face_encodings = face_recognition.face_encodings(ref_rgb_image, ref_face_locations)

input_directory = "./images/"  # directory for source images
matched_directory = "./matched/"  # directory to save filtered images
os.makedirs(matched_directory, exist_ok=True)


for filename in os.listdir(input_directory):
    image_path = os.path.join(input_directory, filename)
    print("Processing Image: ", image_path)

    image = cv2.imread(image_path)  # reading each image from input directory
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_image)

    if not face_locations:
        print(f"No faces detected in {image_path}")
        continue

    face_encodings = face_recognition.face_encodings(rgb_image, face_locations)
    match_found = False

    for encoding in face_encodings:

        results = face_recognition.compare_faces(
            ref_face_encodings,
            encoding,
            tolerance=0.3,  # tolerance is the threshold for matching images
        )

        if any(results):
            print(f"Match found, moving image: {image_path}")
            shutil.copy(image_path, matched_directory)
            match_found = True
            break

    if not match_found:
        print(f"No match found for {image_path}")
