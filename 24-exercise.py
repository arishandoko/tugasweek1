# Exercise 24
# Write a function definition named reverse_sign that takes in a number and returns the provided number but with the sign reversed.

def reverse_sign(number):
  return number * -1

assert reverse_sign(4) == -4
assert reverse_sign(-5) == 5
assert reverse_sign(1) == 1 * -1
assert reverse_sign(2) == 2 * -1
assert reverse_sign(-3) == -3 * -1
assert reverse_sign(-6) == -6 * -1
print("Exercise 24 is correct.")