# WAP to create a new list of repeated items from the given list.
num = [1, 1, 1, 2, 2, 2, 3, 5, 6, 7, 8, 5, 5, 5, 8]
repeated_num = []
for number in num:
    if num.count(number) > 1 and number not in repeated_num:
        repeated_num.append(number)

print(repeated_num)
