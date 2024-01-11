# Strings are immutable datatypes in Python
# They are also the sequential datatypes i.e. iterables

# Creating an empty string
a = ""
b = ''
c = """
"""
d = '''
'''
e = str()


# Creating non-empty strings
a = "apple"
print(a)
b = 'python is awesome'

# c= "Hello World'  different quotations raise error

c = """
Hello World.
I'm learning python
"""  # We can create multiline strings using triple-quotes. This is also called as docstring



def addition(a, b):
    """

    :param a: this should be an integer
    :param b: this should be another integer
    :return: sum of a and b

    This function adds the two integers and return the sum
    """
    return a + b


# Accessing characters in a string
# Indexing and slicing are used to access the string items
# This is similar to list indexing and list slicing

# Indexing
data = "Python is a high level language"

print(data[0])  # P
print(data[5])  # n
print(data[6])  # " "
print(data[-1])  # e
print(data[-7])  # a
print(data[-33]) # error
print(data[50])  # error


# Slicing
data = "Python is a high level language"

print(data[2:])
print(data[:10])
print(data[3:10])
print(data[-10: -2])
print(data[-3: -9])
print(data[:-3])
print(data[-9:])
print(data[10:4])