import json

with open("students.json", "r") as fp:
    data = json.loads(fp.read())
print(data)  # [{}, {}, {}]
print(type(data))  # List

name = data[2]["name"]
print(name)

