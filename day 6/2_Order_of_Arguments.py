# Order of function arguments must be:
# 1. Positional Argument
# 2. Keyword Argument
# 3. *args
# 4. **kwargs


def addition(a, b=3, c=0):
    return a + b + c


addition(1, 3, c=2)  # valid
# addition(a=2, 3, c=1)  # invalid


def addition(a, b, c, d=1, e=2, *args, **kwargs):
    print(a)  # 1
    print(b)  # 2
    print(c)  # 3
    print(d)  # 4
    print(e)  # 5
    print(*args)  # (6, 7, 8, 12, 13)
    print(**kwargs)  # {"f": 9, "g": 10}


addition(1, 2, 3, 4, 5, 6, 7, 8, 12, 13, f=9, g=10)
