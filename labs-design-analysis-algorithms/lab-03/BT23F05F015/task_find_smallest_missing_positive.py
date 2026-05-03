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

# -------------------------------------------
# TASK: Find the Smallest Missing Positive Integer
# -------------------------------------------

def smallest_missing(arr):
    low, high = 0, len(arr) - 1

    # If 1 is missing at the start
    if arr[0] != 1:
        return 1

    # Binary search for the "gap"
    while low <= high:
        mid = (low + high) // 2

        # Ideal value at index mid should be mid + 1
        if arr[mid] == mid + 1:
            low = mid + 1  # missing number is on the right
        else:
            high = mid - 1  # missing number is on the left

    # After loop, 'low' will be at the missing position
    return low + 1


# Example tests
print(smallest_missing([1, 2, 3, 5, 6]))  # Output: 4
print(smallest_missing([2, 3, 4, 5]))     # Output: 1
print(smallest_missing([1, 2, 3, 4, 5]))  # Output: 6

