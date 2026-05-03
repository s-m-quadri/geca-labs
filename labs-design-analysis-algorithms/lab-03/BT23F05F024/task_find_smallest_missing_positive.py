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
    """
    Find the smallest missing positive integer in a sorted array.
    Uses binary search to efficiently locate the first gap.
    """
    if not arr or arr[0] > 1:
        return 1

    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

       
        if arr[mid] == mid + 1:
            low = mid + 1
        else:
          
            high = mid - 1

   
    return low + 1

# Test cases
print("Test Case 1:")
arr1 = [1, 2, 3, 5, 6]
result1 = find_smallest_missing_positive(arr1)
print(f"Input: {arr1}")
print(f"Output: {result1}")
print()

print("Test Case 2:")
arr2 = [2, 3, 4, 5]
result2 = find_smallest_missing_positive(arr2)
print(f"Input: {arr2}")
print(f"Output: {result2}")
print()

print("Test Case 3:")
arr3 = [1, 2, 3, 4, 5]
result3 = find_smallest_missing_positive(arr3)
print(f"Input: {arr3}")
print(f"Output: {result3}")
print()

print("Test Case 4 (empty array):")
arr4 = []
result4 = find_smallest_missing_positive(arr4)
print(f"Input: {arr4}")
print(f"Output: {result4}")
print()

print("Test Case 5:")
arr5 = [3, 4, 5, 6]
result5 = find_smallest_missing_positive(arr5)
print(f"Input: {arr5}")
print(f"Output: {result5}")