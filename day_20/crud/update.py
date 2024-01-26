import json
filename = "students.json"


def update_student():
    id = input("Enter the id of the student: ")
    key = input("Enter the data you want to update: ")
    value = input(f"Enter the new {key}: ")

    with open(filename, "r+") as fp:
        students = json.loads(fp.read())
        for student in students:
            if student["id"] == id:
                student[key] = value

        fp.seek(0)
        fp.write(json.dumps(students, indent=2))

    choice = input("Do you want to continue? (y/n): ")
    return True if choice.lower() == "y" else False