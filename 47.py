# Exercise 47
# Write a function definition named starts_with_vowel that takes in string and True if the string starts with a vowel
def starts_with_vowel(string):
    # Define a set of vowels
    vowels = set('aeiou')
    if string and string[0] in vowels:
        return True
    return False

assert starts_with_vowel("ubuntu") == True
assert starts_with_vowel("banana") == False
assert starts_with_vowel("mango") == False
print("Exercise 47 is correct.")