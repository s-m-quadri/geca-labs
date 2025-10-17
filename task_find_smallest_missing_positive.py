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
    left, right = 0, len(arr) - 1

    # Edge case: missing number is 1
    if arr[0] != 1:
        return 1

    while left <= right:
        mid = (left + right) // 2
        # If the value at mid equals its position + 1, missing number is on the right
        if arr[mid] == mid + 1:
            left = mid + 1
        else:
            # Gap found, missing number could be mid + 1 or on the left
            right = mid - 1

    # After the loop, left points to the smallest missing number
    return left + 1

# Test cases
print(smallest_missing([1, 2, 3, 5, 6]))  # Output: 4_
