# Lists are sequential datatypes in python i.e. they are iterables.
# Lists are mutable datatypes
# Creating lists

a = []  # empty list
b = list()  # empty list

a = [1, 2, 3]  # non-empty list

# list can contain mixed datatypes
b = ["a", 1, 2, "apple", [1, 2, 3]]


# Accessing list elements
# List elements can be accessed using indexing and slicing

# Indexing
# Forward indexing begins from 0 whereas backward indexing starts from -1
vowels = ["a", "e", "i", "o", "u"]
print(vowels[0])  # a
print(vowels[3])  # o
print(vowels[-1])  # u
print(vowels[-4])  # e
# print(vowels[10])  # IndexError. List index out of range
# print(vowels[-7])  # IndexError. List index out of range


# Slicing
data = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(data[0:7])  # ["a", "b", "c", "d", "e", "f", "g"]
print(data[:5])  # ["a", "b", "c", "d", "e"]

print(data[2:8])  # ["c", "d", "e", "f", "g", "h"]
print(data[3:])  # ["d", "e", "f", "g", "h", "i", "j"]

print(data[-7:])  # ["d", "e", "f", "g", "h", "i", "j"]
print(data[:-5])  # ["a", "b", "c", "d", "e"]

print(data[-8:-3])  # ["c", "d", "e", "f", "g"]
print(data[3:-2])  # ["d", "e", "f", "g", "h"]

print(data[8:2])  # []
print(data[-3:-7])  # []