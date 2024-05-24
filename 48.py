# Exercise 48
# Write a function definition named ends_with_vowel that takes in string and True if the string ends with a vowel
def ends_with_vowel(string):
    # Define a set of vowels
    vowels = set('aeiou')
    if string and string[-1] in vowels:
        return True
    return False

assert ends_with_vowel("ubuntu") == True
assert ends_with_vowel("banana") == True
assert ends_with_vowel("mango") == True
assert ends_with_vowel("spinach") == False
print("Exercise 48 is correct.")