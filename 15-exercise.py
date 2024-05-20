# Exercise 15
# Write a function definition named is_even that takes in a number and returns True or False if that number is even.
def is_even(number):
  if (number % 2 == 0):
    return (True)
  else :
    return (False)

assert is_even(2) == True, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_even(1) == False, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_even(2) == True, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_even(-1) == False, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_even(-2) == True, "Ensure that the function is defined, named properly, and returns the correct value"
print("Exercise 15 is correct.")