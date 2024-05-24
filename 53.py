# Exercise 53
# Write a function definition named forth that takes in sequence and returns the forth value of that sequence.
def forth(sequence):
  if sequence:
    return sequence[3]
  else:
    return None
assert forth("ubuntu") == "n"
assert forth([1, 2, 3, 4]) == 4
assert forth(["python", "is", "awesome", "right?"]) == "right?"
print("Exercise 53 is correct.")