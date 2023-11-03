from flask import Flask, render_template, request, redirect, session, jsonify
import face_recognition
from mtcnn.mtcnn import MTCNN
from PIL import Image, ImageDraw
import numpy as np
import cv2
import sqlite3

detector = MTCNN()
app = Flask(__name__,template_folder='template')

# Proff_ID = "A"

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/dashboard',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Proff_ID = password

        conn = sqlite3.connect('face_recognition.db')
        cursor = conn.cursor()
        cursor.execute(f"SELECT PROF_ID FROM PROFF WHERE NAME = '{username}'")
        user = cursor.fetchone()[0]
        conn.close()
    if user == int(password) :
        return  render_template('dashboard.html')
    else : 
        return "DON'T try to become smart"

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
        cv2.imwrite('known_face_.jpg', face)

        conn = sqlite3.connect('face_recognition.db')
        cursor = conn.cursor()

        cursor.execute("SELECT NAME,ENROLLMENT_No, IMAGE FROM STUDENT")
        known_faces = cursor.fetchall()
        for name,data, known_image in known_faces:
            known_face = cv2.imdecode(np.frombuffer(known_image, np.uint8), cv2.IMREAD_COLOR)
            cv2.imwrite(f'known_face_{data}.jpg', known_face)


            S = face_recognition.face_encodings(face_recognition.load_image_file(f'known_face_{data}.jpg'))[0]


            known_face_encodings = [
                S
            ]
            known_face_names = [
                f'{data}'
            ]

            unknown_image = face_recognition.load_image_file("known_face_.jpg")

            face_locations = face_recognition.face_locations(unknown_image)
            face_encodings = face_recognition.face_encodings(unknown_image, face_locations)


            pil_image = Image.fromarray(unknown_image)
            draw = ImageDraw.Draw(pil_image)

            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):

                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)


                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]

                    # print(int(Proff_ID))
                    # if int(Proff_ID) == 106 :
                    #     Subject = "SUBJECT_1"
                    #     print(Subject)
                    # else : 
                    #     Subject = "SUBJECT_2"
                        # print(Subject)
                    print(name)
                    cursor.execute(f"UPDATE ATTENDANCE SET SUBJECT_1 = 1 WHERE ENROLLMENT_No ={name}")
                    conn.commit()

        cursor.execute("SELECT ENROLLMENT_No,SUBJECT_1 FROM ATTENDANCE")
        Data = cursor.fetchall()
        conn.close()
        return render_template('upload.html' ,Data=Data)

if __name__ == '__main__':
    app.run(debug=False)

