# There might occur exceptions and errors while writing programs and those errors must be handled
# properly. Python provides try...except block to handle such errors.


# Errors can be broadly classified as:
# 1. Syntactic Error
# 2. Non-Syntactic Error

# Non-syntactic error can be further classified as:
# 1. ValueError         #eg: int("Python") # Cannot convert string into integer.
# 2. TypeError          #eg: print(2 + "sam") # Cannot add string and integer.
# 3. KeyError           #eg: dict = {"a" : "jon", "b" : "bon"} print(dict["c"]) # c is not in dict.
# 4. IndexError         #eg: list = [1, 2, 3] print(list[12]) # List does not contain 13th element.
# 5. ZeroDivisionError  #eg: 5/0 # Cannot divide by zero.
# 6. NameError          #eg: print(A) # A has not been defined.


try:
    num = int(input("Enter a number: "))
except:
    num = int(input("Enter a proper number: "))

else:
    print(num)


def main():
    try:
        num = int(input("Enter a number: "))
    except:
        print("Enter a valid number.")
        main()
    else:
        print(num)


main()