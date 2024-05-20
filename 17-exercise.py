# Exercise 17
# Write a function definition named is_positive_odd that takes in a number and returns True or False if the value is both greater than zero and odd

def is_positive_odd(number):
  if (number > 0 and number % 2 == 1):
    return (True)
  else :
    return(False)

assert is_positive_odd(3) == True, "Double check your syntax and logic" 
assert is_positive_odd(5) == True, "Double check your syntax and logic"
assert is_positive_odd(6) == False, "Double check your syntax and logic"
assert is_positive_odd(-5) == False, "Double check your syntax and logic"
assert is_positive_odd(-6) == False, "Double check your syntax and logic"
print("Exercise 17 is correct.")