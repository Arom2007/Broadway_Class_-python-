# Create a class Person with instance attributes name and age.
# Create a method get_details in this class to print name and age.
# Create another class Employees with attributes salary and designation and inherits Person class.
# Create a method get_details in this class to print name, age, salary and designation of the Employee.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"Name of person is {self.name}, Age of person is {self.age}"


class Employees(Person):
    def __init__(self, name, age, salary, designation):
        super().__init__(name, age)
        self.salary = salary
        self.designation = designation

    def get_details(self):
        return f"Name of employee is {self.name}, Age of employee is {self.age}, " \
               f"Salary of employee is {self.salary} and Designation of employee is {self.designation}"


employee1 = Employees(name="Ram", age=33, salary="Rs. 35,000", designation="HRM")
print(employee1.get_details())
