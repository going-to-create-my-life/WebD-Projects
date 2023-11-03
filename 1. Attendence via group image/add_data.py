import sqlite3
import cv2
import numpy as np

# # Read an image file
# image_11= cv2.imread('NELSON MANDELA.JPG')
# image_1=cv2.imread('DARSHAN RAVAL.jpg')
# image_2=cv2.imread('KARISHMA KAPOOR.jpg')
# image_3=cv2.imread('ARMAAN MALIK.jpg')
# image_4=cv2.imread('ALMAAN MALIK.jpg')
# image_5=cv2.imread('PRIYANKA CHOPRA.jpg')
# image_6=cv2.imread('KARTIK ARYAN.jpg')
# image_7=cv2.imread('ANU MALIK.jpg')
# image_8=cv2.imread('ARIJIT SINGH.jpg')
# image_9=cv2.imread('SONU NIGAM.jpg')
# image_10=cv2.imread('NARENDRA MODI.jpg')

# # Convert the image to binary data
# img11 = cv2.imencode('.JPG', image_11)[1].tobytes()
# img1=cv2.imencode('.jpg',image_1)[1].tobytes()
# img2=cv2.imencode('.jpg',image_2)[1].tobytes()
# img3=cv2.imencode('.jpg',image_3)[1].tobytes()
# img4=cv2.imencode('.jpg',image_4)[1].tobytes()
# img5=cv2.imencode('.jpg',image_5)[1].tobytes()
# img6=cv2.imencode('.jpg',image_6)[1].tobytes()
# img7=cv2.imencode('.jpg',image_7)[1].tobytes()
# img8=cv2.imencode('.jpg',image_8)[1].tobytes()
# img9=cv2.imencode('.jpg',image_9)[1].tobytes()
# img10=cv2.imencode('.jpg',image_10)[1].tobytes()

# Connect to the database
conn = sqlite3.connect('face_recognition.db')
cursor = conn.cursor()


# # Insert data into the STUDENT table
# cursor.execute("INSERT INTO STUDENT (ENROLLMENT_No,NAME,IMAGE)VALUES (?,?,?)",(1,'DARSHAN RAVAL',img1))
# cursor.execute("INSERT INTO STUDENT (ENROLLMENT_No,NAME,IMAGE)VALUES (?,?,?)",(2,'KARISHMA KAPOOR',img2))
# cursor.execute("INSERT INTO STUDENT (ENROLLMENT_No,NAME,IMAGE)VALUES (?,?,?)",(3,'ARMAAN MALIK',img3))
# cursor.execute("INSERT INTO STUDENT (ENROLLMENT_No,NAME,IMAGE)VALUES (?,?,?)",(4,'ALMAAN MALIK',img4))
# cursor.execute("INSERT INTO STUDENT (ENROLLMENT_No,NAME,IMAGE)VALUES (?,?,?)",(5,'PRIYANKA CHOPRA',img5))
# cursor.execute("INSERT INTO STUDENT (ENROLLMENT_No,NAME,IMAGE)VALUES (?,?,?)",(6,'KARTIK ARYAN',img6))
# cursor.execute("INSERT INTO STUDENT (ENROLLMENT_No,NAME,IMAGE)VALUES (?,?,?)",(7,'ANU MALIK',img7))
# cursor.execute("INSERT INTO STUDENT (ENROLLMENT_No,NAME,IMAGE)VALUES (?,?,?)",(9,'SONU NIGAM',img9))
# cursor.execute("INSERT INTO STUDENT (ENROLLMENT_No,NAME,IMAGE)VALUES (?,?,?)",(10,'NARENDRA MODI',img10))
# cursor.execute("INSERT INTO STUDENT (ENROLLMENT_No,NAME,IMAGE)VALUES (?,?,?)",(8,'ARIJIT SINGH',img8))
# cursor.execute("INSERT INTO STUDENT (ENNT_No,NAME,IMAGE)VALUES (?,?,?)", (11, 'NELSON MANDELA', img11))

# # Insert data into the PROFF table
# cursor.execute("INSERT INTO PROFF (PROF_ID, NAME) VALUES (?, ?)", (104, 'BALA SUBRSUBJECT'))
# cursor.execute("INSERT INTO PROFF (PROF_ID, NAME) VALUES (?, ?)", (106, 'NARAYAN'))

# # Insert data into the ATTENDANCE table
# cursor.execute("INSERT INTO ATTENDANCE (ENROLLMENT_No,SUBJECT_1,SUBJECT_2)VALUES (?,?,?)",(1,0,0))
# cursor.execute("INSERT INTO ATTENDANCE (ENROLLMENT_No,SUBJECT_1,SUBJECT_2)VALUES (?,?,?)",(2,0,0))
# cursor.execute("INSERT INTO ATTENDANCE (ENROLLMENT_No,SUBJECT_1,SUBJECT_2)VALUES (?,?,?)",(3,0,0))
# cursor.execute("INSERT INTO ATTENDANCE (ENROLLMENT_No,SUBJECT_1,SUBJECT_2)VALUES (?,?,?)",(4,0,0))
# cursor.execute("INSERT INTO ATTENDANCE (ENROLLMENT_No,SUBJECT_1,SUBJECT_2)VALUES (?,?,?)",(5,0,0))
# cursor.execute("INSERT INTO ATTENDANCE (ENROLLMENT_No,SUBJECT_1,SUBJECT_2)VALUES (?,?,?)",(6,0,0))
# cursor.execute("INSERT INTO ATTENDANCE (ENROLLMENT_No,SUBJECT_1,SUBJECT_2)VALUES (?,?,?)",(7,0,0))
# cursor.execute("INSERT INTO ATTENDANCE (ENROLLMENT_No,SUBJECT_1,SUBJECT_2)VALUES (?,?,?)",(8,0,0))
# cursor.execute("INSERT INTO ATTENDANCE (ENROLLMENT_No,SUBJECT_1,SUBJECT_2)VALUES (?,?,?)",(9,0,0))
# cursor.execute("INSERT INTO ATTENDANCE (ENROLLMENT_No,SUBJECT_1,SUBJECT_2)VALUES (?,?,?)",(10,0,0))
# cursor.execute("INSERT INTO ATTENDANCE (ENROLLMENT_No,SUBJECT_1,SUBJECT_2)VALUES (?,?,?)",(11,0,0))
cursor.execute("UPDATE ATTENDANCE SET SUBJECT_1 = 0 WHERE ENROLLMENT_No =9")
# Commit the changes and close the database connection
conn.commit()
conn.close()
