import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()

cursor.execute("select * from Student")
studentList = cursor.fetchall()

for student in studentList:
    print(student)

connection.commit()
connection.close()