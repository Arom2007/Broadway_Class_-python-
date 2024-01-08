# Classes are the blueprints of an object
# Objects are the instance of a class


class Person:
    # We can write either properties or methods inside a class
    age = 20  # property / class attribute
    address = "KTM"  # property / class attribute

    def __init__(self, name, email):  # Constructor Method
        # This constructor is called while creating an object
        self.name = name  # instance attribute
        self.email = email  # instance attribute

    def description(self):  # method
        return f"Name is {self.name}, Age is {self.age}, Email is {self.email} and" \
               f" Address is {self.address}"


person1 = Person("Jon", "j@email.com")  # Person1 is an object / instance
print(person1.age)  # 20
print(person1.address)  # KTM
print(person1.name)  # Jon
print(person1.email)  # j@email.com
print(person1.description())

person1.name = "Ram"
print(person1.name)  # Ram

