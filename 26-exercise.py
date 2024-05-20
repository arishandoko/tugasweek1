# Exercise 26
# Write a function definition named is_multiple_of_three that takes in a number and returns True or False if the number is evenly divisible by 3.
def is_multiple_of_three(number):
  if (number % 3 == 0):
    return (True)
  else :
    return(False)

assert is_multiple_of_three(3) == True
assert is_multiple_of_three(15) == True
assert is_multiple_of_three(9) == True
assert is_multiple_of_three(4) == False
assert is_multiple_of_three(10) == False
print("Exercise 26 is correct.")