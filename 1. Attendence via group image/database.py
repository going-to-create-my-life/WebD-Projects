import sqlite3

conn = sqlite3.connect('face_recognition.db')
cursor = conn.cursor()

# Execute the first CREATE TABLE statement
cursor.execute('''
CREATE TABLE IF NOT EXISTS STUDENT (
    ENROLLMENT_No INTEGER PRIMARY KEY,
    NAME VARCHAR(30),
    IMAGE BLOB
);
''')

# Execute the second CREATE TABLE statement
cursor.execute('''
CREATE TABLE IF NOT EXISTS PROFF (
    PROF_ID INTEGER PRIMARY KEY,
    NAME VARCHAR(30)
);
''')

# Execute the third CREATE TABLE statement
cursor.execute('''
CREATE TABLE IF NOT EXISTS ATTENDANCE (
    ENROLLMENT_No INTEGER PRIMARY KEY,
    SUBJECT_1 INTEGER DEFAULT '0',
    SUBJECT_2 INTEGER DEFAULT '0'
);
''')

conn.commit()
conn.close()