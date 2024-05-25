# Exercise 66
# Write a function definition named get_smallest_number that takes in sequence of numbers and returns the smallest number.
def get_smallest_number(sequence):
  return min(sequence)
assert get_smallest_number([1, 3, 2]) == 1
assert get_smallest_number([5, -5, -4, -3, -2, -1, 1, 2, 3, 4]) == -5
assert get_smallest_number([-4, -3, 1, -10]) == -10
print("Exercise 66 is correct.")