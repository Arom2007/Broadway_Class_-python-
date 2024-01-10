# Write a python class named Rectangle constructed from length and width.
# Write a method that will compute the area of a rectangle

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area_of_rectangle(self):
        area = self.length * self.width
        return f"Area of the rectangle is {area} metre square."

example = Rectangle(2,3)
print(example.area_of_rectangle())