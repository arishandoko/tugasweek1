# Exercise 86
# Write a function definition named get_values_not_in_common that takes two lists and returns a single set with the values that each list does not have in common
def get_values_not_in_common(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    unique_to_list1 = set1 - set2
    unique_to_list2 = set2 - set1
    not_in_common_set = unique_to_list1.union(unique_to_list2)
    return not_in_common_set
assert get_values_not_in_common([5, 1, 2, 3], [3, 4, 5, 5]) == {1, 2, 4}
assert get_values_not_in_common([1, 1], [2, 2, 3]) == {1, 2, 3}
assert get_values_not_in_common(["tomato", "mango", "kiwi"], ["eggplant", "tomato", "broccoli"]) == {"mango", "kiwi", "eggplant", "broccoli"}
print("Exercise 86 is correct.")