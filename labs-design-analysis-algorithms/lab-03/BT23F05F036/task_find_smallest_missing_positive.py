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
    low, high = 0, len(arr) - 1
    
    # If the array is perfect (e.g., [1,2,3]), the answer is the next number.
    ans = len(arr) + 1

    while low <= high:
        mid = low + (high - low) // 2
        
        # In a perfect array of positive integers starting from 1, arr[i] should be i + 1.
        # If arr[mid] is greater than what it should be, it means the gap
        # is at or before this position.
        if arr[mid] > mid + 1:
            ans = mid + 1
            high = mid - 1
        # If arr[mid] is at its correct position, the gap must be to the right.
        else:
            low = mid + 1
            
    return ans

# Example test cases
arr1 = [1, 2, 3, 5, 6]
print(f"Input: {arr1}")
print(f"Output: {find_smallest_missing_positive(arr1)}")

print("-" * 20)

arr2 = [2, 3, 4, 5]
print(f"Input: {arr2}")
print(f"Output: {find_smallest_missing_positive(arr2)}")

print("-" * 20)

arr3 = [1, 2, 3, 4]
print(f"Input: {arr3}")
print(f"Output: {find_smallest_missing_positive(arr3)}")

print("-" * 20)

arr4 = []
print(f"Input: {arr4}")
print(f"Output: {find_smallest_missing_positive(arr4)}")