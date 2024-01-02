# Boolean are immutable datatypes
# True and False are the boolean data types in Python
# True and False are also the keyword to represent boolean

# Operations that give boolean type
# 1. Comparison Operation (>, <, >=)
# 2. Logical Operation (and, or, not)
# 3. Membership Operation (in, not in)
# 4. Identity Operation (is, is not)


# Booleans are the subclass of integers in python where True equals to 1 and False equals to 0.

result = True + True
print(result)  # 2

result = 50 * False
print(result)  # 0


# Concept of truthy and falsy in Python

# Truthy
# All the non-empty objects including True itself are the Truthy objects

a = [1, 2, 3]
b = (1, 2, 3)
c = {1, 2, 3}
d = 45
e = -20
f = {"a": 1}
g = "apple"
h = True

print(bool(a))  # True
print(bool(b))  # True
print(bool(c))  # True
print(bool(d))  # True
print(bool(e))  # True
print(bool(f))  # True
print(bool(g))  # True
print(bool(h))  # True


if a:
    print("a is non empty")


# Falsy
# All the empty objects including zero and False itself are the Falsy objects

a = []
b = ()
c = set()
d = 0
e = 0
f = {}
g = ""
h = False
i = None

print(bool(a))  # False
print(bool(b))  # False
print(bool(c))  # False
print(bool(d))  # False
print(bool(e))  # False
print(bool(f))  # False
print(bool(g))  # False
print(bool(h))  # False
print(bool(i))  # False


if a:
    print("a is non empty")
else:
    print("a is empty")