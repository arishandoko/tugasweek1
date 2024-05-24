# Exercise 46
# Write a function definition named remove_vowels that takes in string and returns the string without any vowels
def remove_vowels(input_string):
    vowels = "aeiou"
    return ''.join(char for char in input_string if char not in vowels)

assert remove_vowels("banana") == "bnn"
assert remove_vowels("ubuntu") == "bnt"
assert remove_vowels("mango") == "mng"
assert remove_vowels("QQQQ") == "QQQQ"
print("Exercise 46 is correct.")