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
            high = mid - 1  # keep searching left side
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
            low = mid + 1  # keep searching right side
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return last


def count_occurrences(arr, target):
    first = find_first(arr, target)
    last = find_last(arr, target)
    if first == -1:
        return 0  # target not found
    return last - first + 1


# Example usage
arr1 = [1, 2, 2, 2, 3, 4]
target1 = 2
print("Count:", count_occurrences(arr1, target1))  # Output: 3

arr2 = [5, 5, 5, 5, 5]
target2 = 5
print("Count:", count_occurrences(arr2, target2))  # Output: 5
