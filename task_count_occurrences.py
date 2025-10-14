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
def first_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    first = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            first = mid
            high = mid - 1  # move left
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return first

def last_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    last = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            last = mid
            low = mid + 1  # move right
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return last

def count_occurrences(arr, target):
    first = first_occurrence(arr, target)
    last = last_occurrence(arr, target)
    
    if first == -1:  # target not found
        return 0
    return last - first + 1

# Example test cases:
arr1 = [1, 2, 2, 2, 3, 4]
print(count_occurrences(arr1, 2))  # Output: 3

arr2 = [5, 5, 5, 5, 5]
print(count_occurrences(arr2, 5))  # Output: 5

arr3 = [1, 3, 3, 3, 7, 9]
print(count_occurrences(arr3, 4))  # Output: 0
