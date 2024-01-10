# Encapsulation is the way of hiding the property and methods in programming
# There are three kinds of encapsulated attributes
# 1. Private
# 2. Protected
# 3. Public


class Person:
    def __init__(self, name, age, address):
        self.__name = name  # Private
        self._age = age
        self.address = address

    def get_info(self):
        return f"Name is {self.__name} and age is {self._age}, address is {self.address}"


p = Person("Jon", 30, "KTM")
print(p._age)
print(p.address)  # KTM
# print(p.__name)  # Jon