# Exercise 12
# Write a function definition named is_positive that takes in a number and returns True or False if that number is positive.
def is_positive(number):
  if (number > 0 ):
    return (True)
  else :
    return(False)

assert is_positive(1) == True, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_positive(2) == True, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_positive(-1) == False, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_positive(-2) == False, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_positive(0) == False, "Zero is not a positive number."
print("Exercise 12 is correct.")