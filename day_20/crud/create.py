import json, os
filename = "students.json"
def create_student():
    id = input("Enter student's id: ")
    name = input("Enter student's name: ")
    age = input("Enter student's age: ")
    address = input("Enter student's address: ")
    student = {"name": name, "age": age, "address": address}

    if not os.path.exists(filename):
        with open(filename, "w") as fp:
            data = json.dumps([student], indent=2)
            fp.write(data)
    else:
        with open(filename, "r+") as fp:
            data = json.loads(fp.read())
            data.append(student)
            fp.seek(0)
            fp.write(json.dumps(data, indent=2))
    choice = input("Do you want to continue? (y/n): ")
    return True if choice.lower() == "y" else False
