# WAP to add all the items in a list.
sum_of_numbers = 0
numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in numbers1:
    sum_of_numbers += x
print("Sum of all numbers in the list is " +str(sum_of_numbers))

# WAP to multiply all the items in a list.
product_of_numbers = 1
numbers2 = [3, 3, 8]
for x in numbers2:
    product_of_numbers *= x
print("Product of all the numbers in the list is " +str(product_of_numbers))

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
strings1 = ['abc', 'xyz', 'aba', '1221', '4884', 'dbdcd', 'laml']
count = 0
for x in strings1:
    if len(x) >= 2 and x[0] == x[-1]:
        count += 1
print("The number of strings in the list with 2 or more letters and the first and last letter being the same is " + str(count))

# WAP to get a list , sorted in increasing order by the last element in each tuple from a list of non-empty tuples.
