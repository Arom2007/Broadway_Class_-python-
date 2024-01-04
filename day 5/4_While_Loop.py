# While loop is used in conditions
# The loop runs until the condition is satisfied and breaks once the condition is not met
# The condition variable must be updated inside the while loop. Otherwise, it runs infinitely


num = 10
while num != 0:
    print(num)
    num -= 1


# Sometimes we may require infinite loop. It can be created as:
#
# while True:
#     print("Infinite")