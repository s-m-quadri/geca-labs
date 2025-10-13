

def smallest_missing_positive(arr):
    n = len(arr)
    left, right = 0, n - 1
    missing = n + 1  

    while left <= right:
        mid = (left + right) // 2

        # If value matches its expected position, search right
        if arr[mid] == mid + 1:
            left = mid + 1
        else:
            # mismatch found, could be the answer
            missing = mid + 1
            right = mid - 1

    return missing


# Test cases
print(smallest_missing_positive([1, 2, 3, 5, 6]))  # Output: 4
print(smallest_missing_positive([2, 3, 4, 5]))     # Output: 1
print(smallest_missing_positive([1, 2, 3, 4, 5]))  # Output: 6


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

