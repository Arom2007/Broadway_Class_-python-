# WAP to create a dictionary student with keys id, name, age, department.
# Take an input from the use, which info(id, name, age, department) he wants to access and print the result.
# Handle the possible exceptions.

student = {"id": 9851, "name": "Rajesh", "age": 44, "department": "accounting"}


def main():
    key = str(input("Enter which info to access: "))

    try:
        value = student[key]
    except KeyError:
        print("Enter a valid key.")
        main()
    else:
        print(value)

main()



