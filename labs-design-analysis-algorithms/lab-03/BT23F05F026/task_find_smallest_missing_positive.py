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
    l, r = 0, len(arr) - 1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == m + 1:
            l = m + 1
        else:
            r = m - 1
    return l + 1

print(smallest_missing([1, 2, 3, 5, 6]))  # Output: 4
print(smallest_missing([2, 3, 4, 5]))    # Output: 1
