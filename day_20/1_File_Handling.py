# Files can be opened, closed and updated using python.
# We can open file in different modes.

# 1. Read mode (r)
# 2. Write mode (w)
# 3. Append mode (a)
# 4. Read and write mode (r+)
# 5. Write and read mode (w+)
# 6. Exclusive write mode (x)

# File can be opened using open() built-in function

fp = open("test.txt", "w")
fp.write("Hello World")
fp.close()

fp = open("test.txt", "r")
data = fp.read()
fp.close()
print(data)

fp = open("test.txt", "a")
fp.write("\nI am learning Python")
fp.close()

# We actually use context managers to open a file. If we open files using context managers then we do not have
# to explicitly close the file.

with open("test.txt", "r") as fp:
    data = fp.read()
print(data)


with open("test.txt", "w") as fp:
    fp.write("Python is a high level language")


with open("test.txt", "r+") as fp:
    data = fp.read()
    fp.write("\nHello World Again")
print(data)


with open("test.txt", "w+") as fp:
    fp.write("\nI also learned Django")
    data = fp.read()
print(data)