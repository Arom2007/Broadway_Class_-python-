# JSON stands for Javascript Object Notation.
# It looks similar to python dictionary.
# It is a data format which can be used for communication between two or more entities.

import json

student = {'name': 'Jon', 'age': 20, 'email': 'j@email.com'}  # Dictionary (Single & double quote can be used)
student1 = {"name": "Jon", "age": 20, "email": "j@email.com"}  # Valid JSON (Only single quotes can be used)

filename = "student.json"

with open(filename, "w") as fp:
    data = json.dumps(student1)
    fp.write(data)

students = [
    {"name": "Jon", "age": 20, "email": "jon@email.com"},
    {"name": "Jane", "age": 19, "email": "jane@email.com"},
    {"name": "Jack", "age": 21, "email": "jack@email.com"},
    {"name": "James", "age": 22, "email": "james@email.com"},
    {"name": "Julie", "age": 20, "email": "julie@email.com"}
]

filename1 = "students.json"

with open(filename1, "w") as fp:
    data = json.dumps(students, indent=2)
    fp.write(data)
