import json
filename = "students.json"

def read_student():
    id = input("Enter the id of the student: ")
    with open(filename, "r") as fp:
        students = json.loads(fp.read())
        for student in students:
            if student['id'] == id:
                print(student)

        choice = input("Do you want to continue? (y/n): ")
        return True if choice.lower() == "y" else False