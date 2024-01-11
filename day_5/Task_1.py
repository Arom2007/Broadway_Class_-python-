# WAP to take a number as input. If the number is divisible by 3, then print 'fizz', if it divisible
# by 5, print 'buzz', if it divisible by both 3 and 5, then print 'fizzbuzz'. If it is not divisible by 3 and
# 5 then print the number as it is.

num1 = int(input("Enter a number: "))
if num1 % 3 == 0 and num1 % 5 != 0:
    print("fizz")
elif num1 % 5 == 0 and num1 % 3 != 0:
    print("buzz")
elif num1 % 3 == 0 and num1 % 5 == 0:
    print("fizzbuzz")
else:
    print(num1)
