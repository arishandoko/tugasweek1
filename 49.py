# Exercise 49
# Write a function definition named starts_and_ends_with_vowel that takes in string and returns True if the string starts and ends with a vowel
def starts_and_ends_with_vowel(string):
    # Define a set of vowels
    vowels = set('aeiou')
    if string and string[-1] and string[0] in vowels:
        return True
    return False
assert starts_and_ends_with_vowel("ubuntu") == True
assert starts_and_ends_with_vowel("banana") == False
assert starts_and_ends_with_vowel("mango") == False
print("Exercise 49 is correct.")