# Create a class Cricketer that has the properties name, age and number of match played.
# Create get_info() method that prints all the information.


class Cricketer:
    def __init__(self, name, age, num_matches):
        self.name = name
        self.age = age
        self.num_matches = num_matches

    def get_info(self):
        return f"Name of cricketer is {self.name}, Age of cricketer is {self.age} and" \
                f" Number of matches played by cricketer is {self.num_matches}."


cricketer1 = Cricketer("John", 31, 63)
print(cricketer1.get_info())
