import sqlite3

def insert(name, surname, age):
    connection = sqlite3.connect("school.db")
    cursor = connection.cursor()
    addCommand = """ INSERT INTO Student VALUES {}"""
    data = (name,surname,age)

    cursor.execute(addCommand.format(data))

    connection.commit()
    connection.close()


insert("Esra","Güngör",20)