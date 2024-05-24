# Exercise 52
# Write a function definition named third that takes in sequence and returns the third value of that sequence.
def third(sequence):
    if sequence:
        return sequence[2]
    else:
        return None
assert third("ubuntu") == "u"
assert third([1, 2, 3]) == 3
assert third(["python", "is", "awesome"]) == "awesome"
print("Exercise 52 is correct.")