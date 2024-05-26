# Exercise 85
# Write a function definition named get_values_in_common that takes two lists and returns a single set with the values that each list has in common
def get_values_in_common(list1, list2):
  set1 = set(list1)
  set2 = set(list2)
  set3 = set1.intersection(set2)
  return set3
assert get_values_in_common([5, 1, 2, 3], [3, 4, 5, 5]) == {3, 5}
assert get_values_in_common([1, 2], [2, 2, 3]) == {2}
assert get_values_in_common(["tomato", "mango", "kiwi"], ["eggplant", "tomato", "broccoli"]) == {"tomato"}
print("Exercise 85 is correct.")