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
def first_occurrence(arr, low, high, target):
    if high >= low:
        mid = (low + high) // 2
        if (mid == 0 or arr[mid-1] < target) and arr[mid] == target:
            return mid
        elif arr[mid] >= target:
            return first_occurrence(arr, low, mid-1, target)
        else:
            return first_occurrence(arr, mid+1, high, target)
    return -1

def last_occurrence(arr, low, high, target, n):
    if high >= low:
        mid = (low + high) // 2
        if (mid == n-1 or arr[mid+1] > target) and arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return last_occurrence(arr, low, mid-1, target, n)
        else:
            return last_occurrence(arr, mid+1, high, target, n)
    return -1

def count_occurrences(arr, target):
    n = len(arr)
    first = first_occurrence(arr, 0, n-1, target)
    if first == -1:
        return 0
    last = last_occurrence(arr, 0, n-1, target, n)
    return last - first + 1

print(count_occurrences([1, 2, 2, 2, 3, 4], 2))
print(count_occurrences([5, 5, 5, 5, 5], 5))