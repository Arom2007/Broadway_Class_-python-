# Write a python function to multiply all the numbers in a list.
def product(numbers):
    total = 1
    for num in numbers:
        total *= num
    return total
prod = product([2, 3, 4, 5])
print(f"Product of all numbers in a list is {prod}")
