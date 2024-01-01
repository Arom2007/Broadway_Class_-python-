"""
Operators are the special symbols in a programming language to perform different operations.
Like in any other language, python also has a set of operators. They are:

1. Arithmetic Operators
2. Logical Operators
3. Relational / Comparison Operators
4. Assignment Operators
5. Identity Operators
6. Membership Operators

"""

# 1. Arithmetic Operators

# Floor division operator
a = 5
b = 2
print(a // b)  # this is called a floor division. Here, 2 is the result


# Modulus Operator
print(a % b)  # 1 (It gives remainder of the division)


# 2. Relational Operators (>, <, >=, <=, !=, ==)
# Result of the relational operations are boolean (True or False)


# 3. Logical Operators (and, or, not)
# Result of logical operations are also boolean


# 4. Assignment Operator (=, +=, *=, /=)
# It assigns a value to a variable
a = 3
a = a + 2
print(a)  # 5

a += 3
print(a)  # 8


# 5. Membership Operators ("in" and "not in")
# Result of membership check is also a boolean value

print(2 in [1, 2, 3])  # True
print(3 not in (1, 2, 3))  # False

print(5 in [1, 2, 3])  # False
print(6 not in [1, 2, 3])  # True


# 6. Identity Operator ("is" and "is not")
# It checks whether the objects are in the same memory location or not
# Result of this operation is also a boolean value