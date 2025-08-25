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
    merged_list = []
    i, j = 0, 0

    # Traverse both lists and append the smaller element to merged_list
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # If there are remaining elements in list1, append them
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    # If there are remaining elements in list2, append them
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list
# Example usage
list1 = [1, 3, 5]
list2 = [2, 4, 6]           

result = merge_sorted_lists(list1, list2)
print(result)  # Output: [1, 2, 3, 4, 5, 6]
