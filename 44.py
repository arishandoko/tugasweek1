# Exercise 44
# Write a function definition named has_vowels that takes in value and returns True if the string contains any vowels.
def has_vowels(value):
    # Define a set of vowels for easy checking
    vowels = set('aeiou')
    
    # Check if any character in the value is a vowel
    for char in value:
        if char in vowels:
            return True
    return False
  
  
assert has_vowels("banana") == True
assert has_vowels("ubuntu") == True
assert has_vowels("QQQQ") == False
assert has_vowels("wyrd") == False
print("Exercise 44 is correct.")