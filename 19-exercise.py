# Exercise 19
# Write a function definition named is_negative_odd that takes in a number and returns True or False if the value is both less than zero and odd.
def is_negative_odd(number):
  if (number < 0 and number % 2 != 0):
    return (True)
  else :
    return(False)

assert is_negative_odd(-3) == True, "Double check your syntax and logic" 
assert is_negative_odd(3) == False, "Double check your syntax and logic"
assert is_negative_odd(4) == False, "Double check your syntax and logic"
assert is_negative_odd(-1) == True, "Double check your syntax and logic"
assert is_negative_odd(-2) == False, "Double check your syntax and logic"
print("Exercise 19 is correct.")
