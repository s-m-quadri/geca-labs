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
    left, right = 0, len(arr) - 1
    first = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            first = mid
            right = mid - 1  
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return first


def last_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    last = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            last = mid
            left = mid + 1   
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return last


def count_occurrences(arr, target):
    first = first_occurrence(arr, target)
    last = last_occurrence(arr, target)
    if first == -1 or last == -1:
        return 0
    return last - first + 1



print(count_occurrences([1, 2, 2, 2, 3, 4], 2))  
print(count_occurrences([5, 5, 5, 5, 5], 5))    