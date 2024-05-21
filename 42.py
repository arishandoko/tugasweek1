import math
# Exercise 42
# Write a function definition named circumference that takes in a number representing a circle's radius and returns the circumference.
def circumference(radius):
  pi = math.pi
  return 2*pi*radius

assert circumference(3) == 18.84955592153876
assert circumference(5) == 31.41592653589793
assert circumference(7) == 43.982297150257104
print("Exercise 42 is correct.")