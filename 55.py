# Exercise 55
# Write a function definition named second_to_last that takes in sequence and returns the second to last value of that sequence.
def second_to_last(sequence):
  if sequence:
    return sequence[-2]
  else:
    return None
assert second_to_last("ubuntu") == "t"
assert second_to_last([1, 2, 3, 4]) == 3
assert second_to_last(["python", "is", "awesome"]) == "is"
assert second_to_last(["kiwi", "mango", "guava"]) == "mango"
print("Exercise 55 is correct.")