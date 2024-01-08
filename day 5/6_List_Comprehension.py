num = [1, 2, 3, 4, 5, 6, 7, 8]
result = []

for i in num:
    result.append(i*2)

print(result)  # [2, 4, 6, 8, 10, 12, 14, 16]


# Using List Comprehension

result = [i*2 for i in num]
print(result)   # [2, 4, 6, 8, 10, 12, 14, 16]


result = [i for i in num if i % 2 == 0]
print(result)  # [2, 4, 6, 8]
