# Write a python function to check whether a given number falls within a given range.
def is_in_range(num, ran):
    return num in ran


num = int(input("Enter a number: "))
in_range = is_in_range(num, range(1, 100))
print(in_range)
