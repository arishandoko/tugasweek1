# Exercise 61
# Write a function definition named mean that takes in sequence of numbers and returns the average value
def mean(sequence):
  total = sum(sequence)
  count = len(sequence)
  average = total/count
  return average
  

assert mean([1, 2, 3, 4]) == 2.5
assert mean([3, 3, 3]) == 3
assert mean([1, 5, 6]) == 4
print("Exercise 61 is correct.")