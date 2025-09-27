# Puzzle / Learning focus:
# - You are given a “mountain array” (numbers increase then decrease).
# - Your task is to find the peak element using binary search ideas.
# - Think carefully about how to compare neighbors to detect the peak.
#
# Example test cases:
# Input: [1, 3, 7, 12, 9, 5, 2]
# Output: 12
#
# Input: [0, 2, 4, 6, 3, 1]
# Output: 6
def find_peak_element(arr):
    """
    Find the peak element in a mountain array using binary search.
    A mountain array increases then decreases, so there's exactly one peak.
    """
    if not arr:
        return None

    if len(arr) == 1:
        return arr[0]

    low, high = 0, len(arr) - 1

    while low < high:
        mid = (low + high) // 2

        # If we're on the ascending part of the mountain
        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        # If we're on the descending part of the mountain
        else:
            high = mid

    # When low == high, we've found the peak
    return arr[low]

def find_peak_index(arr):
    """
    Find the index of the peak element in a mountain array.
    """
    if not arr:
        return -1

    if len(arr) == 1:
        return 0

    low, high = 0, len(arr) - 1

    while low < high:
        mid = (low + high) // 2

       
        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        
        else:
            high = mid

    return low

def find_peak_with_validation(arr):
    """
    Find peak with additional validation for mountain array property.
    """
    if not arr:
        return None

    peak_idx = find_peak_index(arr)
    peak_val = arr[peak_idx]

    print(f"Peak found at index {peak_idx} with value {peak_val}")
    return peak_val


print("Test Case 1:")
arr1 = [1, 3, 7, 12, 9, 5, 2]
result1 = find_peak_with_validation(arr1)
print(f"Input: {arr1}")
print(f"Output: {result1}")
print()

print("Test Case 2:")
arr2 = [0, 2, 4, 6, 3, 1]
result2 = find_peak_with_validation(arr2)
print(f"Input: {arr2}")
print(f"Output: {result2}")
print()

print("Test Case 3 (single element):")
arr3 = [5]
result3 = find_peak_with_validation(arr3)
print(f"Input: {arr3}")
print(f"Output: {result3}")
print()

print("Test Case 4 (two elements):")
arr4 = [1, 2]
result4 = find_peak_with_validation(arr4)
print(f"Input: {arr4}")
print(f"Output: {result4}")
print()

print("Test Case 5:")
arr5 = [10, 20, 30, 40, 50, 45, 35, 25, 15, 5]
result5 = find_peak_with_validation(arr5)
print(f"Input: {arr5}")
print(f"Output: {result5}")