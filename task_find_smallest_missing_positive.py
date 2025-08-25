# Puzzle / Learning focus:
# - Given a sorted array of positive numbers, find the smallest missing positive integer.
# - Use binary search thinking to locate the “gap” without checking every element.
# - Challenge: handle edge cases at the start and end of the array.
#
# Example test cases:
# Input: [1, 2, 3, 5, 6]
# Output: 4
#
# Input: [2, 3, 4, 5]
# Output: 1


def smallest_missing(arr, low, high):
    if low > high:
        return high + 2
    mid = (low + high) // 2
    if arr[mid] == mid + 1:
        return smallest_missing(arr, mid + 1, high)
    else:
        return smallest_missing(arr, low, mid - 1)

def find_smallest_missing(arr):
    if not arr or arr[0] != 1:
        return 1
    return smallest_missing(arr, 0, len(arr) - 1)

print(find_smallest_missing([1, 2, 3, 5, 6]))  # 4
print(find_smallest_missing([2, 3, 4, 5]))     # 1