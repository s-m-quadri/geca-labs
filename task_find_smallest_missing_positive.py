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
def smallest_missing(arr):
    low, high = 0, len(arr) - 1

    # Edge case: if first number > 1, then 1 is missing
    if arr[0] != 1:
        return 1

    # Binary search for the gap
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == mid + 1:
            low = mid + 1  # go right
        else:
            high = mid - 1  # go left

    # When loop ends, low points to the place where pattern breaks
    return low + 1








