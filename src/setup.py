
import mysql.connector
import sqlite3

class DBclass:
    def __init__(self, path):
        self.path = path
        self.db = sqlite3.connect(path)
        self.cursor = self.db.cursor()

    def execute(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def commit(self):
        self.db.commit()

db = DBclass('data.db')
# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="priet",
    password="Priet@007",
    database="priet"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM data")
list = mycursor.fetchall()
# print(list)


# db.execute("DROP TABLE IF EXISTS students")
# TABLE ALREADY CREATED SO COMMENTING THIS OUT
create_table_query = """CREATE TABLE students (
  rollno INT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL,
  branch VARCHAR(255) NOT NULL,
    section varchar(255)
)"""


# SETUP CODE BELOW
# db.execute(create_table_query)

for item in list:
    rollno = item[0]
    name = item[1]
    namesplit = name.split()
    email = ""
    for i in range(len(namesplit)-1):
        email += namesplit[i]
        email += "."
    email += namesplit[len(namesplit)-1]
    email = email.lower()

    branch = item[2]

    section = item[3]
    chk = branch.lower()
    if (chk == "cse" or chk == "ece"):
        email += "@students.iiit.ac.in"
    else:
        email += "@research.iiit.ac.in"
    # print(email)
    # INSERT CODE BELOW
    insert_query = f"""INSERT INTO students VALUES ({rollno}, "{name}", "{email}", "{branch}", "{section}")"""
    db.execute(insert_query)
    db.commit()