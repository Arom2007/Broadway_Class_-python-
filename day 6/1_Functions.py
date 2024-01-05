# Functions are the block of reusable code
# Function in Python can be created using 'def' keyword
# function name follows rules of identifier naming


def addition(a, b):   # function definition
    return a + b  # function return


result = addition(2, 3)  # function call


# Types of function arguments

# 1. Positional Arguments
# 2. Default Arguments
# 3. Arbitrary Arguments



# 1. Positional Arguments
# They are the compulsory arguments


def addition(a, b):
    return a + b

result = addition(2, 3)
print(result)


# 2. Default Arguments
def addition(a, b, c=0):
    return a + b + c


result = addition(2, 3)  # 5
result = addition(2, 5, 6)  # 13

r1 = addition(b=2, a=1, c=4)
print(r1)  # 7


# 3. Arbitrary Arguments
def addition(*args):
    print(args)


addition(1, 2)


def addition(**kwargs):
    print(kwargs)

# Arbitrary Arguments
def addition(*args):
    print(args)
    return sum(args)


s1 = addition(1, 2)
print(s1)  # 3
s2 = addition(1, 2, 3)
print(s2)  # 6
s3 = addition(1, 2, 3, 4)
print(s3)


def addition(**kwargs):
    print(kwargs)
    values = kwargs.values()
    return sum(values)


r1 = addition(a=1, b=2)
print(r1)  # 3
r2 = addition(a=1, b=2, c=3)
print(r2)  # 6
r3 = addition(a=1, b=2, c=3, d=4)
print(r3)  # 10
