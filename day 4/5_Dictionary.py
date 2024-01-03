# Dictionary is a mutable datatype in Python
# Elements in a dict are enclosed in curly braces
# Elements are in the key-value pair format


# Creating dictionary
data = {}  # empty dict
data = dict()  # empty dict

student = {"name": "Jon", "age": 30, "address": "KTM"}
print(student)

student = dict(name="Jon", age=30, address="KTM")
print(student)

student = {"name": "Jon", "addresses": ["KTM", "BKT", "Pokhara"]}
print(student)


# Keys of a dictionary must be immutable datatypes directly or indirectly

student = {1: "Jon", 2: "KTM"}
print(student)


student = {(1, 2): "Jon", "address": "KTM"}
print(student)

# student = {(1, [1, 2]): "Jon", "address": "KTM"}  # invalid


# Accessing dictionary elements
student = {"name": "Jon", "address": "KTM"}
name = student['name']
print(name)  # Jon


student = {(1, 2): "Jon", "address": "KTM"}
name = student[(1, 2)]
print(name)  # Jon

# roll = student["roll"]
# print(roll)  # Error

name = student.get("name")
print(name)  # Jon

roll = student.get("roll")
print(roll)  # None


# Updating dictionary elements
student = {"name": "Jon", "address": "KTM"}
student["roll"] = 30
print(student)  # {"name": "Jon", "address": "KTM", "roll": 30}

student.update(age=25)
print(student)  # {"name": "Jon", "address": "KTM", "roll": 30, "age": 25}