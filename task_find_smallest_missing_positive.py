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
def find_smallest_missing(arr):
    low, high = 0, len(arr) - 1

    # Edge case: if first element is not 1 → smallest missing is 1
    if arr[0] != 1:
        return 1

    # Binary search to find the first “gap” (where arr[i] != i + 1)
    while low <= high:
        mid = (low + high) // 2

        # If the number matches its “ideal” position, move right
        if arr[mid] == mid + 1:
            low = mid + 1
        else:
            # Otherwise, gap is on the left side
            high = mid - 1

    # When loop ends, `low` points to the first missing position
    return low + 1


# Example test cases
print(find_smallest_missing([1, 2, 3, 5, 6]))  # Output: 4
print(find_smallest_missing([2, 3, 4, 5]))     # Output: 1
print(find_smallest_missing([1, 2, 3, 4, 5]))  # Output: 6
