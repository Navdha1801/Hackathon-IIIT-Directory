from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def display_students():
    # Your code to retrieve student data goes here
    students = [
        {'rollno': '101', 'name': 'John Doe', 'email': 'johndoe@example.com', 'branch': 'CSE', 'section': 'A'},
        {'rollno': '102', 'name': 'Jane Smith', 'email': 'janesmith@example.com', 'branch': 'ECE', 'section': 'B'},
        {'rollno': '103', 'name': 'Bob Johnson', 'email': 'bobjohnson@example.com', 'branch': 'ME', 'section': 'A'}
    ]

    return render_template('testhtml.html', students=students)
