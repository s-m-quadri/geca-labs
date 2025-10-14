# Puzzle / Learning focus:
# - Given a sorted array of positive numbers, find the smallest missing positive integer.
# - Use binary search thinking to locate the "gap" without checking every element.
# - Challenge: handle edge cases at the start and end of the array.
#
# Example test cases:
# Input: [1, 2, 3, 5, 6]
# Output: 4
#
# Input: [2, 3, 4, 5]
# Output: 1

def find_smallest_missing_positive(arr):
    # Handle empty array
    if not arr:
        return 1
    
    # Handle missing 1 at the start
    if arr[0] != 1:
        return 1
    
    left, right = 0, len(arr) - 1
    
    # Binary search for the gap
    while left <= right:
        mid = (left + right) // 2
        
        # If the value at mid is equal to its 1-based position,
        # the gap must be in the right half
        if arr[mid] == mid + 1:
            left = mid + 1
        else:
            # Gap is in the left half
            right = mid - 1
    
    # The smallest missing positive number is left + 1
    return left + 1

# Test cases
arr1 = [1, 2, 3, 5, 6]
print(f"Input: {arr1}")
print(f"Smallest missing positive: {find_smallest_missing_positive(arr1)}")

arr2 = [2, 3, 4, 5]
print(f"\nInput: {arr2}")
print(f"Smallest missing positive: {find_smallest_missing_positive(arr2)}")
# Completed the program
