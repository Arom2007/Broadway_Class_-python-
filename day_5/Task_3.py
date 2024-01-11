# WAP to delete all the occurrences of a specified character in a given string.
sentence = "All the occurrences of a specified character in a given string"
remove_letter = input("Enter the letter you want to remove from the string: ")
result = ""
for letter in sentence:
    if letter.upper() == remove_letter.upper():
        continue
    result += letter
print(result)
