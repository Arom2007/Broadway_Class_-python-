# Loops are used to perform repetitive task. For example, printing the first 100 even
# numbers

# There are two types of loops in python. For loop and while loop. Both of them are
# pre-condition loop. There is no post-condition loop in Python (no do-while loop)


# 1. for loop
# For loop is used in an iterable (sequential data). Loop ends once the iteration is
# completed in the sequence

data = [2, 3, 4, 5, 6, 7, 8]
for each in data:
    print(each)


# range() function
# range is a built-in function in python

data = range(5)
print(list(data))  # [0, 1, 2, 3, 4]

data = range(2, 7)
print(list(data))  # [2, 3, 4, 5, 6]

for each in range(1, 11):
    print(each)

for each in range(1, 20, 2):
    print(each)



# enumerate()
vowels = ["a", "e", "i", "o", "u"]


data = enumerate(vowels)
print(list(data))   # [(0, "a"), (1, "e"), (2, "i"), (3, "o"), (4, "u")]

for index, value in enumerate(vowels):
    print(index)  # 0, 1, 2, 3, 4
    print(value)  # a, e, i, o, u
