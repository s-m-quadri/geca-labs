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

def find_smallest_missing_positive(arr):
    if not arr or arr[0] > 1:
        return 1

    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        expected_value = mid + 1

        if arr[mid] == expected_value:
            left = mid + 1
        else:
            right = mid - 1

    return left + 1     

# Example usage:
print(find_smallest_missing_positive([1, 2, 3, 5, 6]))  # Output: 4
print(find_smallest_missing_positive([2, 3, 4, 5]))     # Output: 1

