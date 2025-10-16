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
# ...existing code...

def find_smallest_missing_positive(arr):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        # If the value at mid is equal to its index + 1, missing is on the right
        if arr[mid] == mid + 1:
            low = mid + 1
        else:
            high = mid - 1
    # The smallest missing positive is low + 1
    return low + 1

# Example test cases
print(find_smallest_missing_positive([1, 2, 3, 5, 6]))  # Output: 4
print(find_smallest_missing_positive([2, 3, 4, 5]))     # Output: 1