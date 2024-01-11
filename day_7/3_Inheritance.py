# Inheritance is the process of accessing properties and methods from the
# Parent class to the Child class

# Types of Inheritance in Python OOP
# 1. Single Inheritance
# 2. Multiple Inheritance
# 3. Multilevel Inheritance
# 4. Hierarchical Inheritance
# 5. Hybrid Inheritance


# 1. Single Inheritance
class A:
    x = 1


class B(A):  # Single Inheritance
    y = 3


obj = B()
print(obj.y)  # 3
print(obj.x)  # 1


# 2. Multiple Inheritance
class A:
    x = 1

class B:
    x = 3

class C(A, B):
    y = 2

obj = C()
print(obj.x)  # 1



# Multilevel Inheritance

class A:
    x = 2


class B(A):
    x = 3


class C(B):
    y = 2


obj = C()
print(obj.x)  # 3


# Hierarchical Inheritance
class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(A):
    pass


# Hybrid Inheritance
class A:
    pass


class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

class E(D):
    pass


# MRO (Method Resolution Order) => It sets the priority of the inherited attributes
print(E.mro())
