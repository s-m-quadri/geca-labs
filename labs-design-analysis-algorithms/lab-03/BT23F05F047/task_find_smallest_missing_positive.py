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
    missing = len(arr) + 1  # default if no gap found (e.g. [1,2,3] → missing=4)

    while low <= high:
        mid = (low + high) // 2
        expected = mid + 1   # in a perfect sequence, arr[mid] should equal this

        if arr[mid] == expected:
            # No gap up to mid → go right
            low = mid + 1
        else:
            # Found a gap → candidate answer
            missing = expected
            high = mid - 1

    return missing
print(smallest_missing_positive([1, 2, 3, 5, 6]))
print(smallest_missing_positive([2, 3, 4, 5]))