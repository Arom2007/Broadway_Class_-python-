# Write a python function that accepts a string and counts the number of upper and lower case letters.
def case_counter(string1):
    up_case = 0
    low_case = 0
    for letter in string1:
        if letter == " ":
            continue
        if letter == letter.upper():
            up_case += 1
        else:
            low_case += 1
    return up_case, low_case


upper_count, lower_count = case_counter("The quick Brown Fox")
print(f"Number of uppercase characters is", upper_count, "and lower is ", lower_count)