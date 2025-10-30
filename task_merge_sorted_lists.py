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

def merge_sorted_lists(list1, list2):
    """Merge two sorted lists into one sorted list (ascending)."""
    i = j = 0
    result = []
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    result.extend(list1[i:])
    result.extend(list2[j:])
    return result

if __name__ == "__main__":
    # Example usage
    examples = [
        ([1, 3, 5], [2, 4, 6]),
        ([1, 2, 3], [4, 5, 6]),
        ([1, 3, 5], []),
        ([], [2, 4, 6]),
        ([], [])
    ]
    for list1, list2 in examples:
        print(f"List1: {list1}, List2: {list2} -> Merged: {merge_sorted_lists(list1, list2)}")
