# Polymorphism refers to many forms of the same function or objects

# For example len() function can take multiple types of iterables such as list, string, dictionary etc
# We should also study method overloading and operator overloading in Polymorphism

# Method Overloading

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):   # method to calculate area
        return 3.14 * self.radius ** 2

    def area(self, radius):
        return 3.14 * radius ** 2


c1 = Circle(3)
r = c1.area(10)
print(r)

# We can conclude, method overloading is not possible in Python



# Operator Overloading
# There are different magic methods for different operators in Python
# __add__, __mul__, __sub__ etc. are some examples of magic methods
# They are also known as dunder methods

a = 1
b = 2
r = a + b
print(r)  # 3

r = a.__add__(b)
print(r)  # 3
