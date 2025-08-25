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
    def find_first(arr, target):
        left, right = 0, len(arr) - 1
        first_index = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                first_index = mid
                right = mid - 1  # Look on the left side
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return first_index

    def find_last(arr, target):
        left, right = 0, len(arr) - 1
        last_index = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                last_index = mid
                left = mid + 1  # Look on the right side
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return last_index

    first_index = find_first(arr, target)
    if first_index == -1:
        return 0  # Target not found

    last_index = find_last(arr, target)
    return last_index - first_index + 1



