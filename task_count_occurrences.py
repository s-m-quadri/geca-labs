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

# -------------------------------------------
# TASK: Count Occurrences Using Binary Search
# -------------------------------------------

def first_occurrence(arr, target):
    low, high = 0, len(arr) - 1
    first = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            first = mid
            high = mid - 1  # Keep looking left
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
            low = mid + 1  # Keep looking right
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return last


def count_occurrences(arr, target):
    first = first_occurrence(arr, target)
    last = last_occurrence(arr, target)
    if first == -1:
        return 0  # Target not found
    return last - first + 1


# Example tests
arr1 = [1, 2, 2, 2, 3, 4]
target1 = 2
print("Count:", count_occurrences(arr1, target1))  # Output: 3

arr2 = [5, 5, 5, 5, 5]
target2 = 5
print("Count:", count_occurrences(arr2, target2))  # Output: 5

