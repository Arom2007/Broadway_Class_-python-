# Functions defined inside a class is called method


# append()
a = [1, 2, 3]
a.append(4)
print(a)  # [1, 2, 3, 4]


# extend()
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)  # [1, 2, 3, 4, 5, 6]


# insert()
a = ["e", "f", "h", "i"]
a.insert(2, "g")
print(a)


# remove()
a = ["e", "f", "g", "h", "i"]
a.remove("h")
print(a)  # ["e", "f", "g", "i"]

a.remove("b")  # Error


# pop()
a = ["e", "f", "g", "h", "i"]
result = a.pop(2)
print(result)  # g
print(a)  # ["e", "f", "h", "i"]

a.pop()
print(a)  # ["e", "f", "h"]

# clear()
a = ["e", "f", "g", "h", "i"]
a.clear()
print(a)  # []


# index()
a = ["e", "f", "g", "h", "i"]
result = a.index("g")
print(result)  # 2

a = [1, 2, 4, 4, 5, 4, 3, 2, 4, 1]
a.index(4, 4, 7)  # 5


# count()
a = ["e", "f", "g", "h", "i", "e", "f", "f"]
result = a.count("f")
print(result)  # 3


# sort()
a = [5, 7, 8, 1, 3, 2]
a.sort()
print(a)  # [1, 2, 3, 5, 7, 8]

a.sort(reverse=True)
print(a)  # [8, 7, 5, 3, 2, 1]


# reverse()
a = [5, 7, 8, 1, 3, 2]
a.reverse()
print(a)  # [2, 3, 1, 8, 7, 5]


# copy()
a = [1, 2, 3]
b = a.copy()
print(b)  # [1, 2, 3]
