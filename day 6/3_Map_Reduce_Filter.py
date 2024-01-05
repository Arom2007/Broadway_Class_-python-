# Higher Order Function
# Those functions which take function as an argument are called higher order function
# map(), reduce() and filter() are the builtin higher order function in Python


# map(function, iterable)
# It takes function as first parameter and iterable as second parameter
# map() function maps the element of the iterable to a new data


nums = [1, 2, 3, 4]


def add_five(num):
    return num + 5


result = map(add_five, nums)
print(list(result))  # [6, 7, 8, 9]


# filter(function, iterable)
# It takes function as first parameter and iterable as second parameter
# filter() function selects the element of the iterable and return a new sequence


nums = [1, 2, 3, 4, 5, 6, 7, 8]


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


result = filter(is_even, nums)
print(list(result))  # [2, 3, 6, 8]


# reduce(function, iterable)
# It reduces the iterable to a single number


from functools import reduce

nums = [1, 2, 3, 4, 5]


def sum_all_elements(x, y):
    return x + y


result = reduce(sum_all_elements, nums)
print(result)  # 15
