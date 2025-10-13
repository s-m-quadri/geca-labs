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
# smallest_missing_positive.py
# Find the smallest missing positive number using binary search logic

def smallest_missing_positive(arr):
    low, high = 0, len(arr) - 1

    # If the first element is greater than 1, 1 is missing
    if arr[0] != 1:
        return 1

    while low <= high:
        mid = (low + high) // 2

        # Perfect alignment up to mid
        if arr[mid] == mid + 1:
            low = mid + 1  # Search right
        else:
            high = mid - 1  # Search left

    # When loop finishes, smallest missing = index + 1
    return low + 1


# Example test cases
print(smallest_missing_positive([1, 2, 3, 5, 6]))  # Output: 4
print(smallest_missing_positive([2, 3, 4, 5]))     # Output: 1
print(smallest_missing_positive([1, 2, 3, 4, 5]))  # Output: 6
print(smallest_missing_positive([1]))              # Output: 2
