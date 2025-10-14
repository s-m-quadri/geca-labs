# Puzzle / Learning focus:
# - You have a sorted array with repeated elements.
# - Count how many times a target number appears using binary search logic.
# - Consider how to find the first and last occurrence efficiently.
#
# Example test cases:
# Input: arr = [1, 2, 2, 2, 3, 4], target = 2
# Output: 3
#
# Input: arr = [5, 5, 5, 5, 5], target = 5
# Output: 5

def find_first_occurrence(arr, target):
    """Find the first occurrence of target using binary search"""
    low, high = 0, len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            result = mid
            high = mid - 1  # Continue searching in the left half
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result

def find_last_occurrence(arr, target):
    """Find the last occurrence of target using binary search"""
    low, high = 0, len(arr) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            result = mid
            low = mid + 1  # Continue searching in the right half
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return result

def count_occurrences(arr, target):
    """Count occurrences of target in sorted array using binary search"""
    first = find_first_occurrence(arr, target)

    if first == -1:
        return 0  # Target not found

    last = find_last_occurrence(arr, target)
    return last - first + 1

# Test cases
print("Test Case 1:")
arr1 = [1, 2, 2, 2, 3, 4]
target1 = 2
result1 = count_occurrences(arr1, target1)
print(f"Input: {arr1}, target = {target1}")
print(f"Output: {result1}")
print()

print("Test Case 2:")
arr2 = [5, 5, 5, 5, 5]
target2 = 5
result2 = count_occurrences(arr2, target2)
print(f"Input: {arr2}, target = {target2}")
print(f"Output: {result2}")
print()

print("Test Case 3 (target not found):")
arr3 = [1, 2, 3, 4, 5]
target3 = 6
result3 = count_occurrences(arr3, target3)
print(f"Input: {arr3}, target = {target3}")
print(f"Output: {result3}")