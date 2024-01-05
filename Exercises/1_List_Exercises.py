# WAP to add all the items in a list.
sum_of_numbers = 0
numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in numbers1:
    sum_of_numbers += x
print("Sum of all numbers in the list is " + str(sum_of_numbers))

# WAP to multiply all the items in a list.
product_of_numbers = 1
numbers2 = [3, 3, 8]
for x in numbers2:
    product_of_numbers *= x
print("Product of all the numbers in the list is " + str(product_of_numbers))

# WAP to get the largest number from a list.
numbers3 = [55, 64, 134, 45, 23]
greatest = numbers3[0]
for x in numbers3:
    if x > greatest:
        greatest = x
print("The largest number in the list is " + str(greatest))

# WAP to get the smallest number from a list.
numbers4 = [3, 5, 23, 534645, 43, 1, 24, 23, 0.5]
smallest = numbers4[0]
for x in numbers4:
    if x < smallest:
        smallest = x
print("The smallest number in the list is " + str(smallest))

# WAP to count the number of strings in a list. The string length should be 2 or more and the first and last character of the list should be the same.
strings1 = ['abc', 'xyz', 'aba', '1221', '4884', 'dbd', 'lal']
count = 0
for x in strings1:
    if len(x) >= 2 and x[0] == x[-1]:
        count += 1
print("The number of strings in the list with 2 or more letters and the first and last letter being the same is " + str(count))

# WAP to remove duplicates from a list.
sample_list = [1, 2, 2, 2, 2, 3, 3, 4, 5, 5, 5, 5, 5, 6, 7, 6, 7, 5, 4, 4, 3, 3, 8, 9, 10, 11]
non_repeated_list = []
for num in sample_list:
    if sample_list.count(num) < 2:
        non_repeated_list.append(num)
print(f"The new list without the repeated items is {non_repeated_list}.")

# WAP to check if a list is empty or not.
example_list = [1, 2, 3, 4]
count = 0
for x in example_list:
    count += 1
if count == 0:
    print("List is empty")
else:
    print("List is not empty")

# WAP that takes two lists and returns True if they have at least one common number.
list1 = [1, 3, 4, 5, 3, 6, 7, 9]
list2 = [2, 0, 8, 3, 11, 12]
for x in list1:
    for y in list2:
        if x == y:
            print(True)

# WAP to print the numbers of a specified list after removing even numbers from it.
random_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
sorted_even_numbers = []
for x in random_numbers:
    if x % 2 == 0:
        sorted_list = sorted_even_numbers.append(x)
print(f"The sorted list of even numbers is {sorted_even_numbers}.")

# WAP to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.
rand_list = [0, 3, 4, 7, 9]
rem = 0
for x in rand_list:
    n = x
    for x in range(2, n):
        if n % x == 0:
            rem += 1
if rem > 1:
    print(False)
else:
    print(True)

# WAP to find the index of an item in a specified list.
specified_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
find = int(input("Enter number you want to find in the list: "))
for x in specified_list:
    if x == find:
        found = (specified_list.index(x))

print(f"The index of the item {find} in the list is {found}.")

# WAP to find the number of items in a list.
listy = [0, 1, 2, 3, 4, 5]
county = 0
for x in listy:
    county += 1
print(f"There are {county} number of items in the list.")