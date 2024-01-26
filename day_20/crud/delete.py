import json
filename = "students.json"


def delete_student():
    id = input("Enter the id of the student: ")
    with open(filename, "r") as fp:
        students = json.loads(fp.read())
        for student in students:
            if student["id"] == id:
                students.remove(student)

    with open(filename, "w") as fp:
        fp.write(json.dumps(students, indent=2))



    choice = input("Do you want to continue? (y/n): ")
    return True if choice.lower() == "y" else False
