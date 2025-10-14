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
# Puzzle / Learning focus:
# - You have a sorted array with repeated elements.
# - Count how many times a target number appears using binary search logic.
# - Find the first and last occurrence efficiently.

def count_occurrences(arr, target):
    # Helper to find the first occurrence of target
    def first_occurrence():
        low, high = 0, len(arr) - 1
        first = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                first = mid
                high = mid - 1  # keep searching to the left
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return first

    # Helper to find the last occurrence of target
    def last_occurrence():
        low, high = 0, len(arr) - 1
        last = -1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                last = mid
                low = mid + 1  # keep searching to the right
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return last

    first = first_occurrence()
    if first == -1:
        return 0  # target not found
    last = last_occurrence()
    return last - first + 1


# --------------------------
# Example Test Cases
# --------------------------
print(count_occurrences([1, 2, 2, 2, 3, 4], 2))   # Output: 3
print(count_occurrences([5, 5, 5, 5, 5], 5))      # Output: 5
print(count_occurrences([1, 1, 2, 3, 3, 3, 4], 3)) # Output: 3
print(count_occurrences([1, 2, 3, 4, 5], 6))      # Output: 0
print(count_occurrences([], 2))                   # Output: 0
