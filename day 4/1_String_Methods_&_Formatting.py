# String Methods

# capitalize()
messg = "hello world"
result = messg.capitalize()
print(messg)  # hello world
print(result)  # Hello world


# upper()
messg = "hello world"
print(messg.upper())  # HELLO WORLD

# lower()
messg = "hello world"
print(messg.lower())  # hello world

# title()
messg = "hello world"
print(messg.title())  # Hello World


# split()
messg = "hello world"
result = messg.split()
print(result)  # ["hello", "world"]

messg = "hello+world"
result = messg.split("+")
print(result)  # ["hello", "world"]

messg = "hello world"
result = messg.split("o")
print(result)  # ["hell", " w", "rld"]


# join()
data = ["hello", "world"]
result = "+".join(data)
print(result)  # hello+world

result = " ".join(data)
print(result)  # hello world

result = "".join(data)
print(result)  # helloworld


# string formatting (f-string)
name = "Jon"
age = 30
messg = f"Hello I'm {name} and I'm {age} years old"
print(messg)  # Hello I'm Jon and I'm 30 years old