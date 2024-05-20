# Exercise 14
# Write a function definition named is_odd that takes in a number and returns True or False if that number is odd.
def is_odd(number):
  if (number % 2 != 0):
    return (True)
  else :
    return(False)
assert is_odd(1) == True, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_odd(2) == False, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_odd(-1) == True, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_odd(-2) == False, "Ensure that the function is defined, named properly, and returns the correct value"
print("Exercise 14 is correct.")