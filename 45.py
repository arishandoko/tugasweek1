# Exercise 45
# Write a function definition named count_vowels that takes in value and returns the count of the nubmer of vowels in a sequence.
def count_vowels(value):
    # Define a set of vowels for easy checking
    vowels = set('aeiou')
    
    # Initialize a counter for vowels
    count = 0
    
    # Iterate through each character in the input value
    for char in value:
        # Check if the character is a vowel
        if char in vowels:
            count += 1
    
    # Return the total count of vowels
    return count

assert count_vowels("banana") == 3
assert count_vowels("ubuntu") == 3
assert count_vowels("mango") == 2
assert count_vowels("QQQQ") == 0
assert count_vowels("wyrd") == 0
print("Exercise 45 is correct.")