# keys()
student = {"name": "Jon", "address": "KTM", "age": 30}

keys = student.keys()
print(keys)  # dict_keys(["name", "address", "age"])
print(list(student.keys()))  # ["name", "address", "age"]


# values()
values = student.values()
print(values)  # dict_values(["Jon", "KTM", 30])
print(list(values))  # ["Jon", "KTM", 30]


# items()
items = student.items()
print(items)  # dict_items([("name", "Jon"), ("age", 30), ("address", "KTM")])
print(list(items))  # [("name", "Jon"), ("age", 30), ("address", "KTM")]