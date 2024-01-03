# Set is a mutable datatype but every elements of a set must be immutable
# Set is also sequence of data but the data are enclosed in curly braces {}

# Creating set
a = set()  # empty set
a = {1, 2, 3}  # non-empty set

a = {1, "hello", 3}
# a = {1, 2, [1, 2, 3]}   # list is mutable and a set can't contain a mutable element


# Adding and removing set elements
s = {1, 2, 3}
s.add(4)
print(s)  # {1, 2, 3, 4}

s.update([5, 6, 7])
print(s)  # {1, 2, 3, 4, 5, 6, 7}


s = {1, 2, 3, 4, 5, 6}
s.remove(4)
print(s)  # {1, 2, 3, 5, 6}

s.discard(3)
print(s)  # {1, 2, 5, 6}

s.remove(10)  # it raises error
s.discard(10)  # It doesn't raise error

s.clear()
print(s)  # set()

