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
def is_in_range(num, ran):
    if num in ran:
        return "Number is in range."
    else:
        return "Number is not in range."


num = 34
in_range = is_in_range(num, range(1, 100))
print(in_range)


# Write a python function to multiply all the numbers in a list.
def product(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total


prod = product([1, 2, 3, 4, 5])
print(f"Product of all numbers in the list is {prod}")


# Write a python function that accepts a string and counts the number of upper and lower case letters.
def case_counter(string1):
    up_case = 0
    low_case = 0
    for letter in string1:
        if letter == " ":
            continue
        if letter == letter.upper():
            up_case += 1
        else:
            low_case += 1
    return up_case, low_case


upper_count, lower_count = case_counter("The quick Brown Fox")
print(f"Number of uppercase characters is", upper_count, "and lower is ", lower_count)


# Write a python function to reverse a string.
def reverser(string2):
    rev_string = ""
    n = -1
    for x in string2:
        rev_string += string2[n]
        n -= 1
    return rev_string


s1 = reverser("Hello")
print(s1)


# Write a Python function that takes a list and returns a new list with distinct elements from the first list.
def distinct(list1):
    distinct_list = []
    for x in list1:
        if x not in distinct_list:
            distinct_list.append(x)
    return distinct_list


lest = distinct([1, 2, 3, 3, 3, 3, 4, 5])
print(lest)


# Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
def prime_checker(number_sample):
    count = 2
    div = 0
    while count < number_sample:
        if number_sample % count == 0:
            div += 1
        count += 1
    if div > 1:
        return "Number is not a prime number"
    else:
        return "Number is a prime number"


prime1 = prime_checker(11)
print(prime1)


# Write a Python program to print the even numbers from a given list.
def even_sorter(num_list):
    sorted_list = []
    for x in num_list:
        if x % 2 == 0:
            sorted_list.append(x)
    return sorted_list


num_list1 = even_sorter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(num_list1)

#  Write a Python function that checks whether a passed string is a palindrome or not.
def palindrome(string_test):
    a = string_test
    b = ""
    count = -1
    for letter in string_test:
        b += string_test[count]
        count -= 1
    if a == b:
        return "String is a palindrome."
    else:
        return "String is not a palindrome."


test = palindrome("bad")
print(test)
