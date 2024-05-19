# Exercise 13
# Write a function definition named is_negative that takes in a number and returns True or False if that number is negative.
def is_negative(number):
  if (number < 0 ):
    return (True)
  else :
    return(False)
assert is_negative(1) == False, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_negative(2) == False, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_negative(-1) == True, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_negative(-2) == True, "Ensure that the function is defined, named properly, and returns the correct value"
assert is_negative(0) == False, "Zero is not a negative number."
print("Exercise 13 is correct.")