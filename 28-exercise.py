# Exercise 28
# Write a function definition named is_multiple_of_both_three_and_five that takes in a number and returns True or False if the number is evenly divisible by both 3 and 5.

def is_multiple_of_both_three_and_five(number):
  if (number % 5 == 0 and number % 3 == 0 ):
    return (True)
  else :
    return(False)

assert is_multiple_of_both_three_and_five(15) == True
assert is_multiple_of_both_three_and_five(45) == True
assert is_multiple_of_both_three_and_five(3) == False
assert is_multiple_of_both_three_and_five(9) == False
assert is_multiple_of_both_three_and_five(4) == False
print("Exercise 28 is correct.")