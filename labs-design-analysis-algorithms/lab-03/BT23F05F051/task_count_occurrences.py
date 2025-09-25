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

def count_occurrences(arr, target):
    n = len(arr)

    #  First occurrence 
    left, right = 0, n - 1
    first = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            first = mid
            right = mid - 1  # keep looking left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if first == -1:  # target not found
        return 0

    #  Last occurrence 
    left, right = 0, n - 1
    last = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            last = mid
            left = mid + 1  # keep looking right
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # ---------- Count ----------
    return last - first + 1



arr = [1, 2, 2, 2, 3, 4, 5]
target = 2
print(count_occurrences(arr, target))  # Output: 3
