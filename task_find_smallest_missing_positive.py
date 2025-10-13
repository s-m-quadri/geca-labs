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
    left, right = 0, len(arr) - 1
    
    # edge case: missing 1
    if arr[0] != 1:
        return 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == mid + 1:
            left = mid + 1
        else:
            right = mid - 1
    
    return left + 1

# Example usage

arr1 = [1, 2, 3, 5, 6]
print(smallest_missing_positive(arr1))  # Output: 4

arr2 = [2, 3, 4, 5]
print(smallest_missing_positive(arr2))  # Output: 1
