# Exercise 82
# Write a function definition named longest_string that takes in sequence of strings and returns the longest string in the list.
def longest_string(strings):
    return max(strings, key=len)
assert longest_string(["kiwi", "mango", "strawberry"]) == "strawberry"
assert longest_string(["hello", "everybody"]) == "everybody"
assert longest_string(["mary", "had", "a", "little", "lamb"]) == "little"
print("Exercise 82 is correct.")