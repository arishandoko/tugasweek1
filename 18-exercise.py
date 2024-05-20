# Exercise 18
# Write a function definition named is_positive_even that takes in a number and returns True or False if the value is both greater than zero and even
def is_positive_even(number):
  if (number > 0 and number % 2 == 0):
    return (True)
  else :
    return(False)

assert is_positive_even(4) == True, "Double check your syntax and logic" 
assert is_positive_even(3) == False, "Double check your syntax and logic"
assert is_positive_even(6) == True, "Double check your syntax and logic"
assert is_positive_even(-5) == False, "Double check your syntax and logic"
assert is_positive_even(-6) == False, "Double check your syntax and logic"
print("Exercise 18 is correct.")