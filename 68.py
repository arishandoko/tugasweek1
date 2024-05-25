# Exercise 68
# Write a function definition named only_even_numbers that takes in sequence of numbers and returns the even numbers in a list.
def only_even_numbers(sequence):
    even_numbers = []
    for num in sequence:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

assert only_even_numbers([1, 2, 3]) == [2]
assert only_even_numbers([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]) == [-4, -2, 2, 4]
assert only_even_numbers([-4, -3, 1]) == [-4]
assert only_even_numbers([1, 1, 1, 1, 1, 1]) == []
print("Exercise 68 is correct.")