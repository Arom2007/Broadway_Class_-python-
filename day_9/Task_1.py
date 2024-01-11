# WAP to take 2 numbers as input and add those numbers.
# Handle the possible exceptions.
def main():
    try:
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter a second number: "))
    except ValueError:
        print("Please enter two valid numbers.")
        main()
    else:
        print(num1 + num2)


main()