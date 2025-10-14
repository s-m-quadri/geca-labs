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
    left, right = 0, len(arr) - 1
    first = -1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            first = mid
            right = mid - 1  # Continue searching in the left half
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return first

def find_last_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    last = -1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            last = mid
            left = mid + 1  # Continue searching in the right half
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return last

def count_occurrences(arr, target):
    first = find_first_occurrence(arr, target)
    if first == -1:
        return 0
    last = find_last_occurrence(arr, target)
    return last - first + 1

# Test cases
arr1 = [1, 2, 2, 2, 3, 4]
target1 = 2
print(f"Count of {target1} in {arr1}: {count_occurrences(arr1, target1)}")

arr2 = [5, 5, 5, 5, 5]
target2 = 5
print(f"Count of {target2} in {arr2}: {count_occurrences(arr2, target2)}")
# Completed the program
