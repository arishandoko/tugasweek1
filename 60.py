# Exercise 60
# Write a function definition named sum_all that takes in sequence of numbers and returns all the numbers added together.
def sum_all(sequence):
  return sum(sequence)
assert sum_all([1, 2, 3, 4]) == 10
assert sum_all([3, 3, 3]) == 9
assert sum_all([0, 5, 6]) == 11
print("Exercise 60 is correct.")