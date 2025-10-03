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

def find_first(arr, target):
    low, high = 0, len(arr) - 1
    first = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            first = mid
            high = mid - 1  # Keep searching on the left side
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return first

def find_last(arr, target):
    low, high = 0, len(arr) - 1
    last = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            last = mid
            low = mid + 1  # Keep searching on the right side
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return last

def count_occurrences(arr, target):
    first = find_first(arr, target)
    last = find_last(arr, target)

    if first == -1 or last == -1:
        return 0  # Target not found

    return last - first + 1

print(count_occurrences([1, 2, 2, 2, 3, 4], 2))
print(count_occurrences([5, 5, 5, 5, 5], 5)) 