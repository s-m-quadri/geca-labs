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

def find_smallest_missing(arr):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == mid + 1:
            left = mid + 1
        else:
            right = mid - 1
            
    return left + 1

# Example test cases:

print(find_smallest_missing([1, 2, 3, 5, 6]))  # Output: 4
print(find_smallest_missing([2, 3, 4, 5]))     # Output: 1
print(find_smallest_missing([]))               # Output: 1


