# Condition statements are used to make decisions in Python
# There are different types of conditions:


# 1. Simple if
a = 5
if a == 5:
    print("The number is 5")


# 2. if...else statement
a = 5
if a == 5:
    print("The number is 5")
else:
    print("The number is not 5")


# 3. if...elif..else ladder

a = 5
if a == 5:
    print("The number is 5")
elif a == 6:
    print("The number is 6")
elif a == 7:
    print("The number is 7")
else:
    print("The number is neither 5, 6 nor 7")


a = 5
if a == 5:
    print("The number is 5")
if a == 6:
    print("The number is 6")
if a == 7:
    print("The number is 7")
else:
    print("The number is neither 5, 6 nor 7")


# ternary if
num = 10
print("Even") if num % 2 == 0 else print("Odd")

