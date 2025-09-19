# You are given two sorted lists `list1` and `list2`.
# Merge them into a single sorted list (ascending order) and return the result.

# Example:
# Input:
# list1 = [1, 3, 5]
# list2 = [2, 4, 6]
# Output:
# [1, 2, 3, 4, 5, 6]

# INSTRUCTIONS:
# - Do NOT use Python's built-in sorted().
# - Implement your own merge function (similar to merge sort's merge step).
# - No recursion required.

# Write your solution here
def merge_sorted_lists(list1, list2):
    merged = []
    i, j = 0, 0

    # Compare elements from both lists and add the smallest to merged
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    # If elements are left in list1, extend merged with them
    while i < len(list1):
        merged.append(list1[i])
        i += 1

    # If elements are left in list2, extend merged with them
    while j < len(list2):
        merged.append(list2[j])
        j += 1

    return merged

# Example usage:
list1 = [1, 3, 5]
list2 = [2, 4, 6]
print(merge_sorted_lists(list1, list2))  # Output: [1, 2, 3, 4, 5, 6]
