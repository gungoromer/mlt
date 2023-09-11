import sqlite3


connection = sqlite3.connect("school.db")
cursor = connection.cursor()
updateCommand = """ UPDATE Student set surname='Rüsgar' where name='Esra'"""


cursor.execute(updateCommand)

connection.commit()
connection.close()
