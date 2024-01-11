class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def get_info(self):
        return f"Name is {self.name} and age is {self.age}"


class Employee(Person):
    def __init__(self, name, age, address, designation):
        super().__init__(name, age)
        self.address = address
        self.designation = designation

    def get_info(self):   # Method overriding
        print(super().get_info())
        return f"address is {self.address} and designation is {self.designation}"


e1 = Employee("Jon", 30, "KTM", "Manager")
print(e1.get_info())
print(e1.address)