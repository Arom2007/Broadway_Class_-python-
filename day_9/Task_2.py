# WAP to take 2 numbers as input and divide a number by another number.
# Handle the possible exceptions.

def main():
    try:
        a = float(input("Enter a number: "))
        b = float(input("Enter another number: "))
        division = a / b
    except ValueError:
        print("Please input two valid numbers.")
        main()
    except ZeroDivisionError:
        print("Please do not use zero as the dividing number.")
        main()
    else:
        print(division)


main()
