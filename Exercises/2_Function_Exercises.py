# Write a python function to find the maximum of 3 numbers.
def maximum(a, b, c):
    if a > b and a > c:
        greatest = a
    elif b > a and b > c:
        greatest = b
    else:
        greatest = c
    return greatest


find_greatest = maximum(1, 2, 3)
print(f"Greatest of the three numbers is {find_greatest}.")


# Write a python function to reverse a string.
def reverse(string_name):

    rev_string = ""
    index = len(string_name)
    while index > 0:
        rev_string += string_name[index-1]
        index -= 1
    return rev_string


print("Reverse of the given string is " + reverse("Aroma"))


# Write a python function to check whether a given number falls within a given range.
def is_in_range(numb, ran):
    if numb in ran:
        return "Number is in range."
    else:
        return "Number is not in range."


numb = int(input("Enter a number: "))
in_range = is_in_range(numb, range(1, 100))
print(in_range)


# Write a python function to multiply all the numbers in a list.
def product(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total


prod = product([1, 2, 3, 4, 5])
print(f"Product of all numbers in the list is {prod}")
