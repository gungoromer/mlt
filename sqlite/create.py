import sqlite3

connection = sqlite3.connect("school.db")

cursor = connection.cursor()

cursor.execute("""Create table IF NOT EXISTS STUDENTS(
               name text,
               surname text,
               age integer
)""")

connection.commit()
connection.close()