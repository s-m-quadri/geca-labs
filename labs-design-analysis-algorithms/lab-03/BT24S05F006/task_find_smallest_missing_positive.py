# Puzzle / Learning focus:
# - Given a sorted array of positive numbers, find the smallest missing positive integer.
# - Use binary search thinking to locate the “gap” without checking every element.
# - Challenge: handle edge cases at the start and end of the array.
#
# Example test cases:
# Input: [1, 2, 3, 5, 6]
# Output: 4
#
# Input: [2, 3, 4, 5]
# Output: 1
def smallest_missing_positive(arr):
    low, high = 0, len(arr) - 1

    # Case 1: If the first element is not 1 → smallest missing is 1
    if arr[0] != 1:
        return 1

    # Binary search for the "gap"
    while low <= high:
        mid = (low + high) // 2

        # Check if missing is on the left side
        if arr[mid] > mid + 1:
            high = mid - 1
        else:
            low = mid + 1

    # At the end, `low` points to the missing position
    return low + 1


# Example test cases
print(smallest_missing_positive([1, 2, 3, 5, 6]))  # Output: 4
print(smallest_missing_positive([2, 3, 4, 5]))     # Output: 1
print(smallest_missing_positive([1, 2, 3, 4, 5]))  # Output: 6
