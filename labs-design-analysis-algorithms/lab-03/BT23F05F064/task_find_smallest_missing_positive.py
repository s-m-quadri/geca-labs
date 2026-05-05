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
    missing = len(arr) + 1 

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] != mid + 1:
            missing = mid + 1  
            right = mid - 1   
        else:
            left = mid + 1    
    return missing


arr1 = [1, 2, 3, 5, 6]
arr2 = [2, 3, 4, 5]
print(smallest_missing_positive(arr1))  
print(smallest_missing_positive(arr2)) 
