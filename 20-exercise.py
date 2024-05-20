# Exercise 20
# Write a function definition named is_negative_even that takes in a number and returns True or False if the value is both less than zero and even.

def is_negative_even(number):
  if (number < 0 and number % 2 == 0):
    return (True)
  else :
    return(False)

assert is_negative_even(-4) == True, "Double check your syntax and logic" 
assert is_negative_even(3) == False, "Double check your syntax and logic"
assert is_negative_even(2) == False, "Double check your syntax and logic"
assert is_negative_even(-1) == False, "Double check your syntax and logic"
assert is_negative_even(-6) == True, "Double check your syntax and logic"
print("Exercise 20 is correct.")