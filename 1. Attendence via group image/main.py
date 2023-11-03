
from flask import Flask, render_template, request, redirect, session, jsonify
import face_recognition
from mtcnn.mtcnn import MTCNN
from PIL import Image, ImageDraw
import numpy as np
import cv2
import sqlite3

detector = MTCNN()
app = Flask(__name__,template_folder='template')


@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/dashboard',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('face_recognition.db')
        cursor = conn.cursor()
        cursor.execute("SELECT PROF_ID FROM PROFF WHERE NAME = ? AND PROF_ID = ?", (username, password))
        user = cursor.fetchone()
        conn.close()

    return  render_template('dashboard.html')
        # if user:
        #     session['username'] = username
        # else:
        #     return 'Invalid username or password.'
        # return render_template('/')





@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

@app.route('/upload', methods=['POST'])
def upload():
        if 'file' not in request.files:
            return 'No file part'

        file = request.files['file']

        if file.filename == '':
            return 'No selected file'

        face = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
        # face = detector.detect_faces(image)
    # for face in faces:
        # x, y, w, h = face['box']
        # face = image[y:y+h, x:x+w]
        cv2.imwrite('known_face_.jpg', face)
    # face = detector.detect_faces(image)

# Connect to the database
        conn = sqlite3.connect('face_recognition.db')
        cursor = conn.cursor()

# Execute a query to retrieve the image data
        cursor.execute("SELECT NAME,ENROLLMENT_No, IMAGE FROM STUDENT")
        known_faces = cursor.fetchall()
        for name,data, known_image in known_faces:
            known_face = cv2.imdecode(np.frombuffer(known_image, np.uint8), cv2.IMREAD_COLOR)
            cv2.imwrite(f'known_face_{data}.jpg', known_face)
# Load a sample picture and learn how to recognize it.

            S = face_recognition.face_encodings(face_recognition.load_image_file(f'known_face_{data}.jpg'))[0]

# Load a second sample picture and learn how to recognize it.
    # R = face_recognition.face_encodings(face_recognition.load_image_file("ARIJIT SINGH.jpg"))[0]

# Create arrays of known face encodings and their names
            known_face_encodings = [
                S
            ]
            known_face_names = [
                f'{data}'
            ]

# Load an image with an unknown face
            unknown_image = face_recognition.load_image_file("known_face_.jpg")

# Find all the faces and face encodings in the unknown image
            face_locations = face_recognition.face_locations(unknown_image)
            face_encodings = face_recognition.face_encodings(unknown_image, face_locations)


            pil_image = Image.fromarray(unknown_image)
            draw = ImageDraw.Draw(pil_image)

# Loop through each face found in the unknown image
            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

                name = "Dundee"

                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]

    # Draw a box around the face using the Pillow module
    # draw.rectangle(((left, top), (right, bottom)), outline=(48, 63, 159))

    # Draw a label with a name below the face
            # text_width, text_height = draw.textsize(name)
    # draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(48, 63, 159), outline=(48, 63, 159))
            # draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 0, 255, 0))


# Remove the drawing library from memory as per the Pillow docs
                    print(name)
                    cursor.execute(f"UPDATE ATTENDANCE SET SUBJECT_1 = 1 WHERE ENROLLMENT_No ={name}")
                    conn.commit()
                    pil_image.show()
        cursor.execute("SELECT ENROLLMENT_No,SUBJECT_1 FROM ATTENDANCE")
        Data = cursor.fetchall()
        conn.close()
        return render_template('upload.html' ,Data=Data)

if __name__ == '__main__':
    app.run(debug=True)

# You can also save a copy of the new image to disk if you want by uncommenting this line
# pil_image.save("image_with_boxes.jpg")