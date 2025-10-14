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
def count_occurrences(arr, target):
    def find_first(arr, target):
        low, high = 0, len(arr) - 1
        first = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                first = mid
                high = mid - 1
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
                low = mid + 1
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return last

    first = find_first(arr, target)
    last = find_last(arr, target)

    if first == -1:
        return 0
    return last - first + 1


def find_smallest_missing(arr):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == mid + 1:
            low = mid + 1
        else:
            high = mid - 1
    return low + 1


# Test cases for count_occurrences
print(count_occurrences([1, 2, 2, 2, 3, 4], 2))   # Output: 3
print(count_occurrences([5, 5, 5, 5, 5], 5))      # Output: 5

# Test cases for find_smallest_missing
print(find_smallest_missing([1, 2, 3, 5, 6]))     # Output: 4
print(find_smallest_missing([2, 3, 4, 5]))        # Output: 1
