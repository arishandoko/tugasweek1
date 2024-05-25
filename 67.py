# Exercise 67
# Write a function definition named only_odd_numbers that takes in sequence of numbers and returns the odd numbers in a list.
def only_odd_numbers(sequence):
    odd_numbers = []
    for num in sequence:
        if num % 2 != 0:
            odd_numbers.append(num)
    return odd_numbers

assert only_odd_numbers([1, 2, 3]) == [1, 3]
assert only_odd_numbers([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]) == [-5, -3, -1, 1, 3, 5]
assert only_odd_numbers([-4, -3, 1]) == [-3, 1]
assert only_odd_numbers([2, 2, 2, 2, 2]) == []
print("Exercise 67 is correct.")