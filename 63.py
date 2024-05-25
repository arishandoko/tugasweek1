# Exercise 63
# Write a function definition named mode that takes in sequence of numbers and returns the most commonly occuring value
from collections import Counter

def mode(sequence):    
    # Use Counter to count the occurrences of each element
    counts = Counter(sequence)
    
    # Find the maximum frequency
    max_count = max(counts.values())
    
    # Find the elements with the maximum frequency
    modes = [num for num, count in counts.items() if count == max_count]
    
    # Return one of the modes (if there are multiple, it will return the first one encountered)
    return modes[0]
assert mode([1, 2, 2, 3, 4]) == 2
assert mode([1, 1, 2, 3]) == 1
assert mode([2, 2, 3, 3, 3]) == 3
print("Exercise 63 is correct.")