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


# Write a python function to check whether a number falls within a given range.
