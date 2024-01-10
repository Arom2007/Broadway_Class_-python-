# Create a class Circle with attributes radius.
# Create two objects of circle c1 and c2.
# Add the radius of the circles and print the result.
# Do the above task using a method and then a magic method.
# Compare the size of the circle and print the result using magic method.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def add_radius(self, other):
        return self.radius + other.radius

    def __add__(self, other):
        return self.radius + other.radius



c1 = Circle(10)
c2 = Circle(5)
sum = c1.add_radius(c2)
print(sum)
sum2 = c1.__add__(c2)
print(sum2)
