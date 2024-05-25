# Exercise 62
# Write a function definition named median that takes in sequence of numbers and returns the average value
def median(lst):
  sorted_lst = sorted(lst)
  n = len(sorted_lst) 
  if n % 2 == 1:
        return sorted_lst[n // 2]
  else:
        mid1 = sorted_lst[n // 2 - 1]
        mid2 = sorted_lst[n // 2]
        return (mid1 + mid2) / 2

assert median([1, 2, 3, 4, 5]) == 3.0
assert median([1, 2, 3]) == 2.0
assert median([1, 5, 6]) == 5.0
assert median([1, 2, 5, 6]) == 3.5
print("Exercise 62 is correct.")