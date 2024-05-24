# Exercise 56
# Write a function definition named third_to_last that takes in sequence and returns the third to last value of that sequence.
def third_to_last(sequence):
  if sequence:
    return sequence[-3]
  else:
    return None
assert third_to_last("ubuntu") == "n"
assert third_to_last([1, 2, 3, 4]) == 2
assert third_to_last(["python", "is", "awesome"]) == "python"
assert third_to_last(["strawberry", "kiwi", "mango", "guava"]) == "kiwi"
print("Exercise 56 is correct.")