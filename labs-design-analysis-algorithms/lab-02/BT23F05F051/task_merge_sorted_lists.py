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
# Function to merge two sorted lists
def merge_sorted_lists(list1, list2):
    i = 0  # Pointer for list1
    j = 0  # Pointer for list2
    result = []

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    while i < len(list1):
        result.append(list1[i])
        i += 1


    while j < len(list2):
        result.append(list2[j])
        j += 1

    return result


if __name__ == "__main__":
    list1 = [1, 3, 5]
    list2 = [2, 4, 6]

    merged_list = merge_sorted_lists(list1, list2)
    print("Merged List:", merged_list)

