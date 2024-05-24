# Exercise 50
# Write a function definition named first that takes in sequence and returns the first value of that sequence.
def first(sequence):
    if sequence:
        return sequence[0]
    else:
        return None

assert first("ubuntu") == "u"
assert first([1, 2, 3]) == 1
assert first(["python", "is", "awesome"]) == "python"
print("Exercise 50 is correct.")