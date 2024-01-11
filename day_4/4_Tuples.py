# Tuple is an immutable datatype
# Tuple elements are enclosed in small brackets ()

# Creating tuple
a = ()  # empty tuple
b = tuple()  # empty tuple
vowel = ("a", "e", "i", "o", "u")  # non-empty tuple


# Accessing tuple elements
# Tuple elements can be accessed using Indexing and Slicing which is similar to List


# Tuple packing and unpacking
x = 1
y = 2

print(x)  # 1
print(y)  # 2

z = x
x = y
y = z

print(x)  # 2
print(y)  # 1

x = 1
y = 2
x, y = y, x
print(x)  # 2
print(y)  # 1


a, b, c = 1, 2, 3
print(a) # 1
print(b) # 2
print(c) # 3


# a, b = 1, 2, 3  # Raises error
# a, b, c = 1, 2  # Raises error


# Tuple methods
# Tuple has only two methods  index() and count() which is similar to list index() and count() methods
