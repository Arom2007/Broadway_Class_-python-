# Calculate the factorial of 5 using:
# 1) Normal function and loop
# 2) reduce() function

num = 1
product = 1
while num < 6:
    product *= num
    num += 1
print(product)


from functools import reduce
range_of_num = range(1, 6)
result = reduce(lambda x, y: x * y, range_of_num)
print(result)