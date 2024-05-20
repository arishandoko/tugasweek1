# Exercise 27
# Write a function definition named is_multiple_of_five that takes in a number and returns True or False if the number is evenly divisible by 5.

def is_multiple_of_five(number):
  if (number % 5 == 0):
    return (True)
  else :
    return(False)

assert is_multiple_of_five(3) == False
assert is_multiple_of_five(15) == True
assert is_multiple_of_five(9) == False
assert is_multiple_of_five(4) == False
assert is_multiple_of_five(10) == True
print("Exercise 27 is correct.")