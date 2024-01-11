# break statement breaks the loop
for i in range(10):
    if i == 6:
        break
    print(i)


# continue statement skips a step and forward to next step
for i in range(10):
    if i == 4:
        continue
    print(i)


# pass statement does nothing
# It is generally used as a placeholder for the future code

def addition(a, b):
    pass


for i in range(10):
    if i == 4:
        pass
    print(i)
