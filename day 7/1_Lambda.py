# Using lambda in maps
nums = [1, 2, 3]
result = map(lambda num: num + 4, nums)
print(list(result))

# Using lambda in filter
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter(lambda num: num % 2 == 0, nums)
print(list(result))

# Using lambda in reduce
from functools import reduce
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = reduce(lambda x, y: x + y, nums)
print(result)

# Lambda is an elegant way to create one-liner function in Python

def addition(x, y):
    return x + y


addition(2, 3)


add = lambda x, y: x + y
add(2, 3)


# map
nums = [1, 2, 3, 4]

result = map(lambda num: num + 5, nums)
print(list(result))  # [6, 7, 8, 9]


# filter

nums = [1, 2, 3, 4, 5, 6, 7, 8]


result = filter(lambda num: num % 2 == 0, nums)
print(list(result))  # [2, 4, 6, 8]


# reduce

from functools import reduce

nums = [1, 2, 3, 4, 5]


def sum_all_elements(x, y):
    return x + y


result = reduce(sum_all_elements, nums)
print(result)  # 15