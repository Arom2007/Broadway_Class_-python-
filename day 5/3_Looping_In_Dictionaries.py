student = {"name": "Jon", "age": 30, "address": "KTM"}

for each in student:
    print(each)  # name, age, address


values = student.values()
for each in values:
    print(each)  # Jon, 30, KTM


keys = student.keys()
for each in keys:
    print(each)  # name, age, address


items = student.items()
for each in items:
    print(each)  # ("name", "Jon")  ("age", 30)   ("address", "KTM")


for key, value in student.items():
    print(key)   # name, age, address
    print(value)  # Jon, 30, KTM
