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
#todo
def count_occurrences(arr, target):
    def find_first():
        left, right = 0, len(arr) - 1
        first = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                first = mid
                right = mid - 1  # go left to find earlier occurrence
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return first

    def find_last():
        left, right = 0, len(arr) - 1
        last = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                last = mid
                left = mid + 1  # go right to find later occurrence
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return last

    first_index = find_first()
    last_index = find_last()

    if first_index == -1:  # target not found
        return 0
    return last_index - first_index + 1

# Test examples
arr1 = [1, 2, 2, 2, 3, 4]
target1 = 2
print(count_occurrences(arr1, target1))  # Output: 3

arr2 = [5, 5, 5, 5, 5]
target2 = 5
print(count_occurrences(arr2, target2))  # Output: 5
