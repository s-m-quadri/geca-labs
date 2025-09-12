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
def first_occurrence(arr, x):
    low, high, res = 0, len(arr) - 1, -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            res = mid
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return res

def last_occurrence(arr, x):
    low, high, res = 0, len(arr) - 1, -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            res = mid
            low = mid + 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return res

def count_occurrences(arr, x):
    first = first_occurrence(arr, x)
    last = last_occurrence(arr, x)
    return last - first + 1 if first != -1 else 0

print(count_occurrences([1, 2, 2, 2, 3, 4], 2))
print(count_occurrences([5, 5, 5, 5, 5], 5))
print(count_occurrences([1, 3, 4, 6], 2))
