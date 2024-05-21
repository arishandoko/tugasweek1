import math
# Exercise 41
# Write a function definition named area_of_circle that takes in a number representing a circle's radius and returns the area of the circle
def area_of_circle(radius):
  pi = math.pi
  return pi* radius**2
assert area_of_circle(3) == 28.274333882308138
assert area_of_circle(5) == 78.53981633974483
assert area_of_circle(7) == 153.93804002589985
print("Exercise 41 is correct.")