# Exercise 58
# Write a function definition named first_and_last that takes in sequence and returns the first and last value of that sequence as a list
def first_and_last(sequence):
  if sequence:
    return [sequence[0],sequence[-1]]
  else:
    return None
assert first_and_last([1, 2, 3, 4]) == [1, 4]
assert first_and_last(["python", "is", "awesome"]) == ["python", "awesome"]
assert first_and_last(["strawberry", "kiwi", "mango", "guava"]) == ["strawberry", "guava"]
print("Exercise 58 is correct.")